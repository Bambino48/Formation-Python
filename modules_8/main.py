"""
Formattage de chaines caracteres
"""
# la concaténation permet de mettre bout en bout des chaines en les additionnant
exemple = "Bonjour" + " tout" + " le" + " mpnde"
print(exemple)

# Utilisation d'une fonction de conversion
exemple = "Vous avez entré le nombre " + str(5)
print(exemple)

# Les f-strings
prenom = "Paul"
print(f"Bonjour, {prenom}!")

a = 5
b = 10
print(f"La multiplication de {a} par {b} est égal à {a * b}")

# Utilisation de la méthode format()
age = 26
phrase = f"J'ai {age} ans".format(age)
print(phrase)

prenom = "Pierre"
age = 26
phrase = f"Je m'appelle {prenom} et j'ai {age} ans".format(p=prenom, a=age)
print(phrase)

# Résumé :
protocole = "https://"
nom_du_site = "Docstring"
extension = "fr"

    # Avec l'opérateur +
url = protocole + nom_du_site + "." + extension
print(url)

    # Avec la méthode format
url = "{}www.{}.{}".format(protocole, nom_du_site, extension)
print(url)
url = f"{protocole}.{domaine}.{extension}".format(protocole=protocole, domaine=nom_du_site, extension=extension)
print(url)

    # Avec les f-string
url = f"{protocole}.{nom_du_site}.{extension}"

# Cas d'utilisation de la methode format

from constants import BONJOUR

user = input("Entrez votre nom d'utilisateur : ")
progression = get_weekly_progress(user)

message_de_bienvenue = BONJOUR.format(prenom=user, nombre_videos = progression)
