""" La différence entre les méthodes et les fonctions
- Une méthode est une fonction qui appartient à un objet
    la fonction sorted(liste)
    la methode sort() → liste.sort()

"""
print("Exemple avec la fonction sorted() :")
liste = [5, 3, 9, 7, 1]
liste = sorted(liste)
print(liste)

print("Exemple avec la méthode sort() :")
liste = [5, 3, 9, 7, 1]
liste.sort()
print(liste)

# Les objets muables et immuables
    # Muable : listes, dictionnaires, sets
liste = [5, 3, 9, 7, 1]
liste.sort()
print(liste)
    # Immuable : chaînes de caractères, nombres
livre = "le seigneur des anneaux"
livre = livre.title()
print(livre)

"""
Remarque : certains methodes peuvent agir directement alors
            d'autres fonctions doivent etre mis dans une variable
            pour qu'elles agissent
"""

# Quelques fonctions supplémentaires

    # la fonction len()
string = "Python"
string = len(string)
print("Le nombre de caractère du mot Python est : ",string)

liste = [1, 2, 3]
liste = len(liste)
print("Le nombre d'élément de la liste est :",liste)

    # la fonction round() permet d'arrondir des valeurs
print("L'arrondie de 2.2 est :",round(2.2))
print("L'arrondie de 2.7 est :",round(2.7))

    # les fonctions min() et max()
print("Le minimum de cette liste est :",min([1, 2, 3]))
print("Le maximum de cette liste est :",max([1, 2, 3]))

    # la fonction sum()
print("La somme de la liste est :",sum([10, 10, 10]))

    # range()
liste = range(5)
print(liste)
liste = range(2, 5)
print(liste)

