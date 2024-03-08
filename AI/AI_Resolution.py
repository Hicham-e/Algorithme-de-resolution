from sympy import symbols, Or, And, Not, simplify_logic, to_cnf

def negation(expr):
    """Calcule la négation d'une expression logique expr."""
    return Not(expr)

def mettre_sous_forme_clauses(expr):
    """Met une expression logique expr sous forme de clauses.
    
    Si expr est une disjonction (Or), renvoie les arguments de expr sous forme de liste.
    Sinon, renvoie expr dans une liste.
    """
    return expr.args if isinstance(expr, Or) else [expr]

def chercher_clauses_resolvantes(clauses):
    """Cherche des paires de clauses réductibles dans la liste de clauses.
    
    Pour chaque paire réductible trouvée, effectue une résolution pour obtenir un nouveau résolvant.
    Si un nouveau résolvant est trouvé, le renvoie. Sinon, renvoie False.
    """
    for i, clause1 in enumerate(clauses):
        for j, clause2 in enumerate(clauses):
            if i != j:
                resolvent = simplify_logic(clause1 | clause2)
                if resolvent != False:
                    return resolvent
    return False

def algorithme_resolution(F):
    """Applique l'algorithme de résolution pour vérifier la validité d'une formule logique F."""
    # Négation de la formule F
    neg_F = negation(F)

    # Conversion de la formule négative en forme normale conjonctive (CNF)
    cnf_F = to_cnf(neg_F)

    # Mise sous forme de clauses
    clauses = mettre_sous_forme_clauses(cnf_F)

    # Boucle de résolution
    while True:
        # Recherche de clauses réductibles
        resolvent = chercher_clauses_resolvantes(clauses)
        
        # Si aucune clause réductible n'est trouvée, la formule est valide
        if resolvent == False:
            return "F est valide"  # Aucune clause vide trouvée, F est valide
        
        # Si une clause réductible vide est trouvée, la formule est invalide
        else:
            return "F est invalide"  # Une clause vide a été trouvée, F est invalide


'''
Exemples d'utilisation

F = Or(p, Not(p))                                          #valide
F = And(Or(p, q), Or(Not(p), q), Or(p, Not(q)))            #valide
F = And(And(p, q), And(Not(p), q))                         #invalide
F = And(And(p, q), And(Not(p), Not(q)))                    #invalide

'''
while True:
    F_input = input("Entrez la formule logique F (0 pour sortir): ")
    if F_input == '0': break
    
    p, q, r = symbols('p q r')
    
    # Convertir la chaîne d'entrée en une expression logique
    F = eval(F_input)  

    print(algorithme_resolution(F))


