"""                     Les structures conditionnelles.
Elles permettent de tester des conditions
Exemples – Le nombre entré par l'utilisateur est-il grand ou égal à 18 ?
         - Le nom d'utilisateur entré est-il dans la base de donnée du site ?
         - Le mot de passe de l'utilisateur contient-il au moins 8 caractères ?

Une condition nous retourne un booléen, c'est-à-dire soit vrai ou soit faux
"""

# Tester une condition avec le mot 'if'
age = 20
if age >= 18:
    print("Vous êtes majeur !")

# Les blocs d'instructions : Par defaut definit par la mise en page
# Imbriquation des blocs
if age >= 18:
    print("Vous êtes majeur !")
    if langage == "Python":
        print("Vous pouvez rentrer")

print("Le script est terminé.")

# Tester plusieur condition if, elif
age = 20
if age >= 18:
    print("Vous êtes majeur !") # ok
elif age < 18:
    print("Vous êtes mineur !")

age = 15
if age >= 18:
    print("Vous êtes majeur !")
elif age < 18:
    print("Vous êtes mineur !") # ok

# Les structures conditionnelles avancées : if, elif, else
utilisateur = "admin"
if utilisateur == "admin":
    print("Accès autorisé !")
else:
    print("Accès refusé...")

utilisateur = "admin"
if utilisateur == "admin":
    print("Accès autoris !") # ok
elif utilisateur == "root":
    print("Accès autoris !")
else:
    print("Accès refusé...")


utilisateur = "root"
if utilisateur == "admin":
    print("Accès autoris !")
elif utilisateur == "root":
    print("Accès autoris !")  # ok
else:
    print("Accès refusé...")


utilisateur = "Paul"
if utilisateur == "admin":
    print("Accès autoris !")
elif utilisateur == "root":
    print("Accès autoris !")
else:
    print("Accès refusé...") # ok

# Les operateurs ternaires
age = 20
if age >= 18:
    majeur = True
else:
    majeur = False

age = 20
majeur = True if age >= 18 else False

# Les operateurs logiques : and, or, not
if utilisateur == "admin" and mot_de_passe == "admin":
    print("Accès autoris !")

# and : il faut que toutes les conditions soient vrai
# or : il faut qu'une des condtions soit vrai
# not : retourne l'inverse d'une condtition
if not utilisateur == "admin":
    print("Accès refusé...")

"""
Les erreurs courrantes avec les conditions:

    - l'operateur : ==
    - l'utilisation de plusieur if au lieu de elif
"""

note = 5
if note < 10:
    print("Vous n'avez pas la moyenne.")
if note >= 10 and note < 14:
    print("Peut mieux faire...")
if note >= 14 and note < 19:
    print("Bravo !")
else:
    print("Vous êtes le meilleur !")

note = 5
if note < 10:
    print("Vous n'avez pas la moyenne.")
elif note >= 10 and note < 14:
    print("Peut mieux faire...")
elif note >= 14 and note < 19:
    print("Bravo !")
else:
    print("Vous êtes le meilleur !")


