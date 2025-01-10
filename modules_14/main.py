"""                         Les boicles
    - Répéter une opération un certain nombre de fois
    - Parcourir des structures de données
    - deux types de boucles en python
        * for
        * while
"""
from importlib.metadata import files

# la boucle for
liste = [23, 45, 76, 89, 21]
for element in liste:
    print(element)

for i in [0, 1, 4, 7, 8]:
    print(i)

for letter in "Python":
    print(letter)

for i in range(10):
    print("Bonjour")

# la boucle while
i = 0
while i < 10:
    print("Bonjour")
    i = i + 1

continuer = "o"
while continuer == "o":
    print("On continue ...")
    continuer = input("Voulez vous continuer ? o/n")


import time

while True:
    print("Sauvegarde en cours...")
    time.sleep(600)

# Une boucle while est executee tant qu'une condition est vraie
# Attention aux boucles infinies

# Les instructions continue et break
    # continue fait passer la boucle directement à la prochaine iteration
liste = ["1", "4", "25", "Paul", "3", "Pierre"]
for element in liste:
    if element.isdigit():
        continue
    print(element)
    # break arrete l'execution de la boucle au complet
for element in liste:
    if element.isdigit():
        continue
    print(element)

# La boucle for else
prenoms = ["Pierre", "Patrik", "Jean", "Marc"]

for prenom in prenoms:
    if prenom == "Patrik":
        print("Patrik a été trouvé !")
        break
else:
    print("Patrick est introuvable...")

"""
Les compréhension de liste permet d'iterer et de filtrer les listes
"""

# Exemple sans comprehension de liste
chiffres = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nbres_positifs = []
for i in chiffres:
    if i > 0:
        nbres_positifs.append(i)

# Exemple de comprehension de liste
chiffres = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nbres_positifs = [i for i in chiffres if i > 0]

# Le cas ou l'on veut modifier la valeur de i
chiffres = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nbres_positifs = [i * 2 for i in chiffres if i > 0]

# les fonctions Any et All : Ces fonctions permettent d'operer sur des listes pour verifier au moins sur une valeur est vrai ou si toutes les valeurs sont vrais
any([False, False, False, True, False])

all([False, False, False, True, False])

all([f.endswith(".jpg") for f in files])

notes = [12, 14, 20, 10, 8]
any([x > 18 for x in notes])