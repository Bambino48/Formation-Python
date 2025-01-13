import random

vie_joueur = 50
vie_ennemi = 50
niveau_potion = 3
passer_tour = False

while True:
    # jeu du joueur
    if passer_tour:
        print("Vous passez votre tour... 🔜")
        passer_tour = False
    else:
        choix_utilisateur = ""
        while choix_utilisateur not in ["1", "2"]:
            choix_utilisateur = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? -> ")

        if choix_utilisateur == "1": # Attaque
            utilisateur_attaque = random.randint(5, 10)
            vie_ennemi -= utilisateur_attaque
            print(f"Vous avez infligé {utilisateur_attaque} points de dégâts à l'ennemi ⚔")
        elif choix_utilisateur == "2" and niveau_potion > 0:
            potion_vie = random.randint(15, 50)
            vie_joueur += potion_vie
            niveau_potion -= 1
            passer_tour = True
            print(f"Vous récupérez {potion_vie} points de vie ❤ ({niveau_potion} ? restantes)")
        else:
            print("Vous n'avez plus de potions...")
            continue

        if vie_ennemi <= 0:
            print("Tu as gagné ?")
            break

        # jeu de l'ennemi
        ennemi_attaque = random.randint(5, 15)
        vie_joueur -= ennemi_attaque
        print(f"L'ennemi vous a infligé  {ennemi_attaque} points de dégâts ⚔")

        if vie_joueur <= 0:
            print("Tu as perdu ?")
            break

        # Resultat
        print(f"Il vous reste {vie_joueur} points de vie.")
        print(f"Il reste {vie_ennemi} points de vie à l'ennemi.")
        print("-" * 50)

print("Fin du jeu.")
