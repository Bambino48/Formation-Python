"""
                                    Projet : calculatrice
Creer une calculatrice en ligne de commande qui demande à l'utilisateur de saisir deux nombres
et qui affiche ensuite le résultat de l'addition de ces deux nombres.

"""

number_1 = int(input("Entrer un nombre: "))
number_2 = int(input("Entrer un nombre: "))
result = f"L'addition du nombre {number_1} + {number_2} est égal à {number_1 + number_2}."
print(result)
