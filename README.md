# Algorithme de résolution pour la logique propositionnelle

## Description
Ce projet implémente un algorithme de résolution pour vérifier la validité des formules en logique propositionnelle. 
L'algorithme utilise la résolution par réfutation pour déterminer si une formule est valide ou non.

## Fonctionnalités
- Négation d'une expression logique
- Conversion en forme normale conjonctive (CNF)
- Recherche de clauses réductibles
- Vérification de la validité d'une formule

## Utilisation
L'utilisateur peut entrer une formule logique en utilisant les opérateurs logiques suivants :
- Et : `And`
- Ou : `Or`
- Négation : `Not`
- Variables propositionnelles : `symbols('p', 'q', 'r')`

L'algorithme affiche "F est valide" si la formule est valide, et "F est invalide" sinon.

Exemples d'utilisation

F = Or(p, Not(p))                                          valide
F = And(Or(p, q), Or(Not(p), q), Or(p, Not(q)))            valide
F = And(And(p, q), And(Not(p), q))                         invalide
F = And(And(p, q), And(Not(p), Not(q)))                    invalide
