#!/usr/bin/env python3
import json, subprocess

def run(cmd,timeout=240):
    return subprocess.run(cmd,capture_output=True,text=True,timeout=timeout)

def build_payload(spec,prompt):
    payload={}; used=False
    for p in spec.get('parameters',[]):
        n=p.get('name',''); l=n.lower(); req=bool(p.get('required',False)); default=p.get('default')
        if l in {'message','prompt','text','query','input','instruction','user_message'}:
            payload[n]=prompt; used=True
        elif l in {'chat_history','history','messages'}: payload[n]=[]
        elif l in {'max_new_tokens','max_tokens','maximum_new_tokens'}: payload[n]=700
        elif l=='temperature': payload[n]=0.1
        elif req and default is None and not used: payload[n]=prompt; used=True
    return payload if used else None

def extract(raw):
    raw=raw.strip()
    try:
        obj=json.loads(raw)
        if isinstance(obj,dict):
            for k in ('Response','response','text','output','message'):
                if isinstance(obj.get(k),str): return obj[k].strip()
    except: pass
    return raw

def invoke(space,prompt):
    info=run(['hf-gradio','info',space],120)
    if info.returncode!=0: return False,'',{'stage':'info','error':(info.stderr or info.stdout)[-1200:]}
    try: api=json.loads(info.stdout)
    except Exception as e: return False,'',{'stage':'decode','error':repr(e)}
    prefs=['/generate','/chat','/predict','/respond','/infer','/run']
    eps=list(api.items()); eps.sort(key=lambda kv:(prefs.index(kv[0]) if kv[0] in prefs else 99,kv[0]))
    errs=[]
    for endpoint,spec in eps:
        payload=build_payload(spec,prompt)
        if payload is None: continue
        p=run(['hf-gradio','predict',space,endpoint,json.dumps(payload,ensure_ascii=False)],240)
        if p.returncode==0 and (p.stdout or '').strip(): return True,extract(p.stdout),{'stage':'predict','endpoint':endpoint}
        errs.append((p.stderr or p.stdout)[-700:])
    return False,'',{'stage':'predict','error':' | '.join(errs[-3:])}
