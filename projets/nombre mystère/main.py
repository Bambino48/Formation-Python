"""
L'ordinateur va choisir un nombre entre 1 et 100 et ton objectif est de trouver ce nombre

Bien entendu, tu as droit un nombre limit d'essais pour trouver le nombre.
"""
# Production personnelle

from random import randint

mystere = randint(1, 10)
nbre_essais = 5
choix = "o"

print("---------------------------------------------------------------- Jeu du monbre mystère ------------------------------------------------------------")

print("Vous allez entrer des nombres entre 1 et 100 et cela 3 fois de suite. \nSi le nombre entré est égal à celui de l'ordinateur vous avez gagné sinon dans le cas vous avez perdu.")

while choix == "o":

    for essai in range(1, nbre_essais + 1):

        while True:
            print("Entrer un nombre entre 1 et 10.")
            try:
                nombre = int(input(f"Essai {essai} >>> "))
                if 1 <= nombre <= 100:
                    break
                else:
                    print("Veillez entrer un nombre entre 1 et 10.")
            except ValueError:
                print("Erreur, vous devez entrer un chiffre.")

    if nombre == mystere:
        print("Bravo, vous avez gagné 🎉🎉🎉")
        print(f"Le nombre mystère est : {mystere}")
        break
    else:
        print("Désolé, vous avez perdu ❌")
    if essai < nbre_essais:
        print(f"Il vous reste {nbre_essais - essai}.")
    if (nbre_essais - essai) == 0:
        print("Pour récommencer une nouvel partie tapez 'o' et pour arrêter tapez 'n'.")
        choix = input(">>> ")
        if choix == "o":
            continue
        elif choix == "n":
            print("Merci pour votre participation et la prochaine.")
            break
        else:
            print("Choix invalide.")
            continue