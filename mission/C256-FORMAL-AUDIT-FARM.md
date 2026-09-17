# C256–C265 — FORMAL AUDIT FARM

Audit the strongest current Collatz claims from the Master Hub.

Current objects:
- accelerated odd Collatz T(x)=(3x+1)/2^{v2(3x+1)};
- valuation words a_i>=1, A_k=sum_{i<k}a_i;
- exact affine form 2^{A_k}x_k=3^k x_0+C_k;
- cycle closure D=2^{A_n}-3^n, D|C_n required;
- mechanical/Sturmian balanced words and first-return windows;
- exact 2-adic cylinder x_0 mod 2^{A_n+1};
- 3-adic endpoint/backward congruence constraints;
- arbitrary-length finite first-return feasibility is under study;
- CYCLES OPEN.

AUDIT TARGETS:
1. Quantifiers: distinguish fixed n, arbitrarily large n, all n.
2. Distinguish local realizability of finite words from cycle closure.
3. Check every divisibility and congruence modulus exactly.
4. Check endpoint conventions and strict/non-strict inequalities.
5. Detect circular use of D|C, minimum assumptions, or rotations.
6. Check asymptotic statements for uniformity in word length.
7. Reject any finite computation as arbitrary-N proof.
8. Check independence claims between agents/models.
9. Re-derive strongest lemmas from definitions.
10. Produce a dependency graph: ACCEPT / REJECT / HOLD.

OUTPUT FORMAT:
CLAIM AUDITED
PREMISES
DERIVATION CHECK
HIDDEN ASSUMPTIONS
COUNTERCASE
STATUS: PROVED / REFUTED / HOLD
IMPACT ON CYCLE PROGRAM

No role may declare CYCLES CLOSED unless it supplies a complete arbitrary-N contradiction with every dependency audited.
