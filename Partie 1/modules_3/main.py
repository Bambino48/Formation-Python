"""                             Python un langage dynamique et fortement type

Pourquoi changer le type d'une variable ?

    - Pour utiliser les opérateurs mathématiques sur les variables
    - Pour faire des comparaisons entre plusieurs variables
    - Exemple : 50 est différent de "50"
    Si on fait 50 + "50" on aura une erreur de type,
    car on veut faire l'addition d'un string avec un int

Un langage dynamique – Pas besoin de dire à Python quel est le type de la variable
                     - On peut changer le type d'une variable a tout moment.
                     - Exemple :
                                    ma_variable = 5
                                    ma_variable = "Hello"
"""

""" Les fonctions de conversions : str et int """
print(" ")
a = "5" # type str
a = int(a) # conversion de type str en type int
print(a) # 5

print(" ")

a = 5
b = "10"
b = int(b)
print(a + b) # 15

print(" ")

""" Afficher le type d'une variable
        Pour afficher le type d'une variable en Python on utilise la fonction type()
"""
a = "10"
print(type(a)) # <class 'str'>

a = 10
print(type(a)) # <class 'int'>

a = 10.0
print(type(a)) # <class 'float'>

# Exemple de saisir d'un utilisateur
nombre = input("Entrez le nombre : ")
print(nombre)
print(type(nombre)) # ici pour connaître le type de la variable saisir par l'utilisateur, on utiliser la fonction typr()