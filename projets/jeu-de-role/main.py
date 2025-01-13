"""
Dans ce projet, on va crer un jeu de rle dans le terminal.

Tu vas te battre contre un ennemi, pouvoir attaquer, prendre une potion et te faire attaquer en retour.
"""
from random import randint

# les variables
vie_joueurs = 50
vie_ennemies = 50
potions = 3
tour = 1

print("Bienvenue sur le jeu de rôle.")

# boucle principale
while vie_joueurs > 0 and vie_ennemies > 0:
    print(f"\n--- Tour {tour} ---")
    print(f"Vie du joueur : {vie_joueurs}.")
    print(f"Vie de l'ennemi : {vie_ennemies}.")
    print(f"Potions restantes : {potions}.")

    # action du joueur
    print("Voulez-vous attaquer (1) ou utiliser une potion (2) ?")
    choix = input(">>> ")
    choix = int(choix)
    if choix == 1:
        # attaque du joueur
        degats = randint(15, 50)
        vie_ennemies -= degats
        print(f"Vous avez attaquez l'ennemi et lui infligez {degats} points de dégâts.")
    elif choix == 2 and potions > 0:
        # utilisation d'une potion
        soin = randint(5, 10)
        vie_joueurs += soin
        potions -= 1
        print(f"Vous utilisez une potion et récupérez le {soin} points de vie.")
    else:
        print("Choix invalide ou plus de potions disponibles.")
        continue

    if vie_ennemies <= 0:
        print("Félicitations ! Vous avez vaincu l'ennemi !")
        break

    # Action de l'ennemi
    degats = randint(5, 15)
    vie_joueurs -= degats
    print(f"L'ennemi vous attaque et vous inflige {degats} points dégâts.")

    if vie_joueurs <= 0:
        print("Vous avez été vaincu par l'ennemi... ")
        break

    tour += 1

print("Merci d'avoir joué !")
