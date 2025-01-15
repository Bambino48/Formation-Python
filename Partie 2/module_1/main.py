# Les chemins de dossiers
# le chemin vers les documents de mon ordinateur : "C:\Users\Ibamb\Documents"
# chemins sur windows résoudre le problème des chemins :
# Méthode 1 : ajout de rawstring
chemin = r"C:\Users\Ibamb\Documents"
print(chemin)
# Méthode 2 : utilisation des anti-slashs a la place des slashs.
chemin = "C:/Users/Ibamb/Documents"
print(chemin)
# Méthode 3 : doubler les slashs
chemin = "C:\\Users\\Ibamb\\Documents"
print(chemin)

# Ouvrir et lire le contenu d'un fichier
    # Ouverture du fichier avec mod read r
chemin_fichier = r"C:\Users\Ibamb\Documents\python.txt"

with open(chemin_fichier, "r") as f:
    """ ouvrir le fichier """
    #ouverture_fichier = f.read()
    #print(ouverture_fichier)
    """ ouvrir le contenu en chaîne de caractère """
    # ouverture_fichier_1 = repr(f.read())
    # print(ouverture_fichier_1)
    """ ouvrir le contenu en liste on utilise la méthode readlines()"""
    # ouverture_fichier_2 = f.readlines()
    # print(ouverture_fichier_2)
    """ ouvrir le contenu dans une liste sans / """
    # ouverture_fichier_3 =f.read().splitlines()
    # print(ouverture_fichier_3)


# Ecrire à l'intérieur d'un fichier
    # La méthode write() écrase le contenu du fichier en le remplaçant par la nouvelle saisi
with open(chemin_fichier, "w") as f:
    f.write("Voici mon premier texte...")
with open(chemin_fichier, "r") as l:
    lecture = l.read()
    print(lecture)
    # La méthode add() permet d'ajouter au contenu présent
with open(chemin_fichier, "a") as l:
    l.write("\nEn python")
with open(chemin_fichier, "r") as l:
    lecture = l.read()
    print(lecture)

# Les fichiers JSON
import json

fichier_json = r"C:\Users\Ibamb\Documents\support.json"

with open(fichier_json, "w") as f:
    json.dump(list(range(3)), f, indent=4) # pour ecrire un fichier json
with open(fichier_json, "r") as f:
    liste = json.load(f) # pour lire un fichier json
    print(liste)

liste.append(4) # pour modifier ou ajouter un fichier json

with open(fichier_json, "w") as f:
    liste = json.dump(liste, f, indent=4)

""" Les erreurs courantes à éviter :
- Les erreurs de mode (r : read, w : write, a : append)
- Oublier de fermer un fichier après ouverture
- Il faut deplcer le curseur avec la methode seek()
"""
""" Les erreurs coutantes avec les fichiers JSON
- On ne peut pas lire un fichier json vide
- pour un fichier avec des accents a l'interieur et pour afficher le contenu il faut utiliser la methode ensure_ascii=False"""




