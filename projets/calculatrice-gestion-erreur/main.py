"""
La version 2 du projet de la calculatrice en ligne de commande avec gestion d'erreur
"""
# nbre_1 = input("Entrer un nombre : ")
# nbre_2 = input("Entrer un nombre : ")
#
# if nbre_1.isdigit() and nbre_2.isdigit():
#     print(f"{nbre_1} + {nbre_2} = {nbre_1 + nbre_2}")
# else:
#     print("Erreur de saisi.")

# choix = "o"
#
# while choix == "o":
#     while True:
#         nombre_1 = input("Entrer un premier nombre: ")
#         if nombre_1.isdigit():
#             print(nombre_1)
#             break
#         else:
#             print("Erreur, veillez entrer un nombre valide.")
#     while True:
#         nombre_2 = input("Entrer un second nombre: ")
#         if nombre_2.isdigit():
#             print(nombre_2)
#             break
#         else:
#             print("Erreur, veillez entrer un nombre valide.")
#     print(f"La somme de {nombre_1} + {nombre_2} = {int(nombre_1) + int(nombre_2)}")
#     choix = input("Pour faire un nouveau calcul tapez 'o' ou pour quitter tapez 'n' ")
# print("Fins du programme.")

while True:
    while True:
        try:
            number1 = int(input("Entrez un premier nombre : "))
            break
        except ValueError:
            print("Erreur :  veillez entrer un nombre valide")
    while True:
        try:
            number2 = int(input("Entrez un deuxième nombre : "))
            break
        except ValueError:
            print("Erreur :  veillez entrer un nombre valide")

    print(f"{number1} + {number2} = {int(number1) + int(number2)}")

    while True:
        continuer = input("Voulez-vous continuer ? (oui/non) : ").lower()
        if continuer == "oui":
            break
        elif continuer == "non":
            print("Merci d'avoir utilisé le programme. Au revoir!")
            exit()
        else:
            print("Voulez-vous continuer ? (oui/non)")