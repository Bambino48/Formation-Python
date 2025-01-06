""" Manipuler les objets de types chaînes de caractères

Lorqu'on utilise une fonction sur un objet, on parle de méthodes.
Il existe beaucoup de fonctions en python.
* les fonctions permettant de faire une modification de la casse
"""
# les méthodes qui permettant de changer la casse
    # upper() mettre la chaine en majuscule
exemple_1 = "Bonjour"
print("Exemple de la fonction upper() :",exemple_1.upper())

    # lower() mettre la chaine en miniscule
print("Exemple de la fonction lower() :",exemple_1.lower())

    # capitalize() mettre la premiere lettre en majuscule
exemple_2 = "bonjour"
print("Exemple de la fonction capitalize() :",exemple_2.capitalize())

    # title() mettre une majuscule au debut de chaque lettre
exemple_3 = "bonjour tout le monde"
print("Exemple de la fonction title() :",exemple_3.title())

""" Remplacer des elements """

# Les méthodes de remplacement
    # la fonction replace() permet de remplacer une partie d'une chaîne de caractère
exemple_1 = "bonjour"
print("Exemple de la fonction replace() :",exemple_1.replace("jour", "soir"))
exemple_2 = "bonjour bonjour bonjour"
print("Exemple de la fonction replace() :",exemple_2.replace("jour", "soir"))
print("Exemple de la fonction replace() :",exemple_2.replace(" ", ""))
print("Exemple de la fonction replace() :",exemple_2.replace(" ", "").replace("jour", "soir"))

    # La fonction strip() permet de retirer de maniere specifique des parties d'une chaine caractere
exemple_3 = " bonjour "
print("Exemple de la fonction strip() :",exemple_3.strip())
exemple_3 = " bon jour"
print("Exemple de la fonction strip() :",exemple_3.strip())
exemple_3 = " bonjour "
print("Exemple de la fonction strip() :",exemple_3.strip(" ujor"))
print("Exemple de la fonction rstrip() :",exemple_3.rstrip(" ujor"))
print("Exemple de la fonction lstrip() :",exemple_3.lstrip(" ujor"))

    # La fonction split() permet de separer les elements en retournant une liste
nombres = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10".split(", ")
print("Exemple de la fonction split() :",nombres)

    # La fonction join() permet de retourner une chaine de caractere
numbers = ", ".join("1, 2, 3, 4, 5, 6, 7, 8, 9, 10".split(", "))
numbers2 = ".".join("1, 2, 3, 4, 5, 6, 7, 8, 9, 10".split(", "))
numbers3 = "-".join("a , b, c, d, e, f, g, h".split(", "))
print("Exemple de la fonction join() : ",numbers)
print("Exemple de la fonction join() : ",numbers2)
print("Exemple de la fonction join() : ",numbers3)

    # la fonction zfill() permet de remplir une sequence avec zeros
carac = "9".zfill(4)
carac2 = "9".zfill(3)
print("Exemple de la fonction zfill() : ",carac)
print("Exemple de la fonction zfill() : ",carac2)

for i in range(100):
    print(str(i).zfill(4))

    # la methode is est utilisé avec les methodes pour verifier
print("Exemple de la fonction islower() : ","bonjour".islower())
print("Exemple de la fonction islower() : ","Bonjour".islower())
print("Exemple de la fonction istitle() : ","Bonjour".istitle())
print("Exemple de la fonction istitle() : ","Bonjour tout le monde".istitle())
print("Exemple de la fonction isdigit() : ","50".isdigit())
print("Exemple de la fonction isdigit() : ","a".isdigit())
print("Exemple de la fonction isdigit() : ","50a".isdigit())

    # la fonction count() permet de compter le nombre d'un caractere dans une phrase
print("Exemple de la fonction count() : ","Bonjour le jour".count("jour"))
print("Exemple de la fonction count() : ","Bonjour le jour".count(" jour"))

    # La fonction find() permet de retrouver une chaine de caractere
print("Exemple de la fonction find() : ","Bonjour le jour".find("jour"))
print("Exemple de la fonction find() : ","Bonjour le jour".find("soir"))
print("Exemple de la fonction rfind() : ","Bonjour le jour".rfind("jour"))
print("Exemple de la fonction index() : ","Bonjour le jour".index("jour"))
#print("Exemple de la fonction index() : ","Bonjour le jour".index("soir"))

    # la fonction endswith() et startswith
print("Exemple de la fonction endswith() : ", "image.png".endswith(".png"))
print("Exemple de la fonction endswith() : ", "image.png".endswith(".jpg"))
print("Exemple de la fonction startswith() : ", "image.png".startswith("image"))
print("Exemple de la fonction startswith() : ", "image.png".startswith("video"))
