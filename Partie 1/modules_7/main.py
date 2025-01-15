"""
Les operateurs mathematiques : + ; - ; * ; / ; % ; // ; **

"""
print(f"L'addition de {5} + {3} est égal à {5 + 3}.")
print(f"La soustration de {3} - {2} est égal à {3 - 2}.")
print(f"La multiplication de {4} * {5} est égal à {4 * 5}.")
print(f"La division  de {6} / {2} est égal à {6 / 2}.")

# Utilisation sur des chaines de caracteres
print("Hello" + " World")
print(" Python" * 3)

# les nouveaux operateurs
print(f"Le modulo de {10} % {2} est égal à {10 % 2}.")
print(f"Le modulo de {6 % 4} est égal à {6 % 4}.")

print(f"La division entière de {10} // {2} est égal à {10 // 2}.")
print(f"La division entière de {10} // {3} est égal à {10 // 3}.")

print(f"La puissance de {2} ** {4} est égal à {2 ** 4}.")

""" 
Les opérateurs d'assignation : += ; -= ; *= ; /= ; %= ; //= ; **=
"""
i = 0
i = i + 1 # incrementation (permet d'ajouter 1 a la valeur de la variable initiale
print(i)
i += 1
print(i)

i = 5
i += 10
print(i)
""" Les opérateurs de comparaisons : > -> plus grand que
                                     < -> plus petit que
                                     >= -> plus grand ou egal a
                                     <= -> plus petit ou egal a
                                     == -> eagle a
                                     != -> different de 
"""

"""
La différence entre le mot is et ==

* == permet de verifier l'egalite des valeurs contenu dans des variables
* is permet de verifier si deux objets sont les memes en memoires
"""
a = [1, 2, 3]
b = [1, 3, ]
print(a == b)
print(a is b)
print(id(a))
print(id(b))
a = 1000
b = 2000
print(a is b)
print(a == b)
b = 1000
print(a is b)
print(a == b)