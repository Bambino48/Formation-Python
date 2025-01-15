""" Quelques modules et fonctions

Un module est fichier python qui contient des fonctions qu'on peut utiliser.

"""

import random

r = random.randint(0, 1)
print(r)

r = random.uniform(0, 1)
print(r)

r = random.randrange(0, 101, 10)
print(r)

import os
# le module os permet de creer et supprimer des dossiers
chemin = "F:\Formation-Python"
    # creation du dossier
dossier = os.path.join(chemin, "dossier", "test") # la fonction join() permet de gerer les slashs du dossier
print(dossier)
# Creation d'un dossier
if not os.path.exists(dossier): #
    os.makedirs(dossier) # makedirs() permet de creer plusieurs dossiers et sous-dossiers
                    # mkdir() permet de creer un seul dossier

os.makedirs(dossier, exist_ok=True) # lorqu'on ne veut pas utiliser une structure conditionnelle comme au-dessus

# Supprimer le dossier : removeddirs()
if os.path.exists(dossier):
    os.removedirs(dossier)

# Chercher de l'aide avec les fonctions dir et help
from pprint import pprint
print(dir(random))
help(random.randint)

# Les objets callables
from pprint import pprint

print(callable(pprint))


