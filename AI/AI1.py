from sympy import symbols, Or, And, Not, simplify_logic, to_cnf

def negation(expr):
    return Not(expr)

def mettre_sous_forme_clauses(expr):
    return expr.args if isinstance(expr, Or) else [expr]

def chercher_clauses_resolvantes(clauses):
    for i, clause1 in enumerate(clauses):
        for j, clause2 in enumerate(clauses):
            if i != j:
                resolvent = simplify_logic(clause1 | clause2)
                if resolvent != False:
                    return resolvent
    return False

def algorithme_resolution(F):
    neg_F = negation(F)
    cnf_F = to_cnf(neg_F)
    clauses = mettre_sous_forme_clauses(cnf_F)
    while True:
        resolvent = chercher_clauses_resolvantes(clauses)
        if resolvent == False:
            return "F est valide"
        else:
            return "F est invalide"
        clauses.append(resolvent)

# Exemple d'utilisation
p, q, r = symbols('p q r')
F = Or(p, Not(p))                          #valide
#F = And(And(p, q), And(Not(p), Not(q)))   #invalide
print(algorithme_resolution(F))