"""                                        Les lists
une liste est une facon en programmation de stocker differents valeurs
listes = []
liste = [1, 3, 4, 5]
liste = [250, "Python", True].
"""

# Ajouter et enlever des elements d'une liste
    # la methode append() permet d'ajouter une valeur
print("Ajouter un élément à une liste :")
liste = []
liste.append(1)
print(liste)
print(" ")
    # la methode extend([]) permet d'ajouter plusieurs valeurs sous forme de liste
print("Ajouter des éléments à une listes :")
liste.extend([2, 5, 7, 8])
print(liste)
print(" ")
    # la methode remove() permet de supprimer un element de la liste
print("Supprimer un élément à une liste :")
liste.remove(7)
print(liste)
print(" ")
# Recuperer un element dans une liste
    # les indices : c'est la position d'un element dans une structure de donnee
print("Récupérer un élément d'une liste par son indice :")
language = ["Python", "C++", "Java"]
print(language[0])
print(language[1])
print(language[2])
print(language[-1])
print(language[-2])
print(language[-3])
print(" ")
    # Utilisation des slices (recuperer des tranches de la liste)
print("Récupérer des éléments d'une liste par un slice :")
list_user = ["Utilisateur_1",
             "Utilisateur_2",
             "Utilisateur_3",
             "Utilisateur_4",
             "Utilisateur_5",
             "Utilisateur_6"]
print("Exemple 1 :",list_user[0:1]) # pour recuperer un seul element
print("Exemple 2 :",list_user[0:2])
print("Exemple 3 :",list_user[:])
print("Exemple 4 :",list_user[:-1])
print("Exemple 5 :",list_user[::2])
print("Exemple 6 :",list_user[1:-2:2])
print("Exemple 7 :",list_user[::-1])
print(" ")

    # D'autres methodes sur les listes
        # index() permet de recuperer l'element grace à son index
print("La methode index() ")
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex", "Max"]
resultat = employes.index("Max")
print("L'index de l'employer est : ",resultat)

        # count() permet de compter le nombre d'element dans une liste
resultat = employes.count("Max")
print("Le nombre de l'element dans la liste est  : ",resultat)

        # sort() permet de trier une liste en mettant en ordre alphabetique
employes.sort()
print(employes)

        # La fonction sorted() permet de trier une liste en ordre alphabetique
resultat = sorted(employes)
print(resultat)

        # la fonction reverse() permet d'inverser une liste
employes.reverse()
print(employes)
print(" ")

# D'autres méthodes pour enlever des éléments dans une liste
        # La methode pop() permet d'enlever un element à partir de son index.
employes.pop(-1)
print(employes)
element = employes.pop(-1)
print("L'élément retirer de la liste est : ",element)
print(employes)
print(" ")
        # La methode clear() permet vider une liste
employes.clear()
print(employes)
print(" ")

# Joindre des éléments d'une liste
        # la methode join() permet de joindre les elements d'une liste avec les chaines de caracteres
liste = ["Python", "est", "un", "langage", "incroyable", "."]
resultat = " ".join(liste)
print(resultat)

# Créer une liste à partir à d'une chaîne de caractères
        # la methode split() permet de separer une liste avec un caractere
courses = "Riz, Pommes, Lait, Salade, Saumon, Beurre"
courses = courses.split(", ")
print(courses)

# Les opérateurs d'appartenance
users = ["Paul", "Pierre", "Marie"]
var = "Paul" in users
print(var)
if "Paul" in users:
    print("Bonjour Paul, bon retour parmi nous!")
if "Paul" in users:
    users.remove("Paul")
    print(users)

test = "Java" in "Javascript"
print(test)

# Les listes imbriquées
listes = ["Python", ["Java", "C++", ["C"]], ["Ruby"]]
var = listes[1][0]
print(var)
var = liste[1][-1][0]
print(var)
# Recuperer le premier element d'une liste
print(listes[0][0])

"""
Les erreurs a eviter avec les listes : - pour recuperer un element dans une liste, on utilise des [] et non des ()
                                       - pour supprimer un element avec la methode rmove, on utiliser le non de l'element et non son indice
                                       pour utiliser l'indice, on prend la methode pop()
"""




