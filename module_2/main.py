"""
Les variables sont l'un des concepts les plus importants de la programmation.

Une variable est un nom associé à une valeur.

"""
bonjour = "Bonjour, bienvenue sur mon site web"
a = 5
b = 10

c = a + b
print(c)
"""
nomDeVariable = objet
"""
nombre = 5
print(nombre)
nombre_2 = 10
print(nombre_2)
nombre = 1
print(nombre)
# Garbage collector permet de nettoyer la memoire de l'ordinateur par python

# la fonction id()
print(id(500))
print(id(500))

a = 500
b = a
print("Emplacement de a : ",id(a))
print("Emplacement de b : ", id(b))

b = 1000
print("Emplacement de b : ",id(b))

""" 
    Différentes affectations possibles :
        * Affectations simples
        * Affectations parallèles
        * Affectations multiples
"""
print(" ")
# affectation simple
a = 5
print("La valeur de a : ",a)
b = 8
print("La valeur de b : ",b)
print(" ")
# affectation parallèle
a, b = 5, 8
print("La valeur de a : ",a)
print("La valeur de b : ",b)
a,b = b,a
print("La valeur de a : ",a)
print("La valeur de b : ",b)
print(" ")
# affectation multiples
a = b = c = 5
print("La valeur de a : ",a)
print("La valeur de b : ",b)
print("La valeur de c : ",c)

print(" ")
"""
Singleton et small integer caching
    Singleton : c'est un objet unique (none, true, false)
    small integer caching : -5 et 256 Pour ces nombres des emplcements sont deja reserves dans la memoire.
    Cela est possible avec les chaines de caracteres dont la longeurs est inferieurs a 20 caracteres.
"""
print(" ")
# Exemple singleton
print(id(True)) # 140710340000640
print(id(True)) # 140710340000640

print(" ")
a = "bonjour"
print(id(a))
b = "bonjour"
print(id(b))

"""
Les regles et les conventions de nommage

    - Les regles a suivre :
                            - Ne peut pas commencer par un chiffre
                            - Ne peut pas contenir d;espaces
                            - Ne peut contenir que des caracteres alpha-numeriques (a-z, A-Z, 0-9) et le tiret du bas(_)
                            - Certains mots sont reserverses(print, True, break, ...)
                            - Exemple de nom non-valide : 75Paris, Site-Web, #lien video, True
                            - Corrections des noms : Paris75, Site_Web; lienVideo, true
    Remarque : les noms de variables sont sensibles a la cast donc prenom != Prenom
    
    - les conventions de nommage : 
                                    Exemple de respect des conventions de nommage :
                                    
                                    paris_75
                                    site_web
                                    lien_video
                                    true 
"""

