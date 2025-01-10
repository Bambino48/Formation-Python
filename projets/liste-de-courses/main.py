"""
Dans ce projet, vous allez devoir crer un programme qui permette de gérer une liste de courses.

Dans cette premire version, on va raliser une version simple de la liste de courses avec la cration
d'une liste en mmoire laquelle on ajoute et on enlève des éléments.

"""
listes = []
option = ["1.Liste", "2.Ajouter", "3.Modifier","4.Suppression", "5.Contenu", "6.Stop"]
numbers = [1, 2, 3, 4, 5, 6]

while True:
    print("Bienvenue dans la liste de courses.")
    for element in option:
        print(element)
    choix = input("Veillez Choisir une option >>> ")
    try:
        choix = int(choix)
        if choix in numbers:
            if choix == numbers[0]:
                print(listes)
            elif choix == numbers[1]:
                article = input("Veuillez entrer un article : ")
                listes.append(article)
                print(listes)
            elif choix == numbers[2]:
                modifier = input("Veuillez entrer l'article à modifier : ")
                if modifier in listes:
                    listes.remove(modifier)
                    nouveau = input("Veuillez entrer le nouveau article : ")
                    listes.append(nouveau)
                    print(listes)
                else:
                    print("Erreur : il n'existe pas dans la liste de courses.")
            elif choix == numbers[3]:
                supprimer = input("Veuillez entrer l'article à supprimer : ")
                if supprimer in listes:
                    listes.remove(supprimer)
                else:
                    print("Article n'existe pas dans la liste de courses.")
            elif choix == numbers[4]:
                print(listes)
            elif choix == numbers[5]:
                arreter = input("Pour arrêter le programme tapez 'o' / 'n' >>> ")
                if arreter == "o":
                    continue
                elif arreter == "n":
                    break
                else:
                    print("Erreur : Veuillez entrer le programme tapez 'o' ou 'n' >>> ")
        else:
            print("Option indisponible !")
    except ValueError:
        print("Erreur : veillez entrer un chiffre valide.")
