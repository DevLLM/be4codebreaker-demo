"""
@author: Minopy
@date: 2024-06-08
   __  __ _____ _   _  ____  _______     __
  |  \/  |_   _| \ | |/ __ \|  __ \ \   / /
  | \  / | | | |  \| | |  | | |__) \ \_/ / 
  | |\/| | | | | . ` | |  | |  ___/ \   /  
  | |  | |_| |_| |\  | |__| | |      | |   
  |_|  |_|_____|_| \_|\____/|_|      |_| 
"""
import random 

# Génération de 100 nombres entiers aléatoires entre 1 et 100 inclusivement
random_numbers = [random.randint(1, 100) for _ in range(100)]

def imprimer_nombres_aleatoires(nombres):
    for nombre in nombres:
        print(nombre)

print("Nombres aléatoires générés : ")
imprimer_nombres_aleatoires(random_numbers)

# Création d'un dictionnaire avec des clés aléatoires et des valeurs
mon_dictionnaire = {f"objet_{i}": i for i in range(1, 51)}

def imprimer_dictionnaire(dico):
    return dico

print("\nDictionnaire aléatoire :")
imprimer_dictionnaire(mon_dictionnaire)

def verifier_pair(nombres):
    nombres_pairs = [num for num in nombres if num % 2 == 0]
    return len(nombres_pairs), nombres_pairs

nombre_de_paires, liste_paires = verifier_pair(random_numbers)
print(f"\nNombre de pairs : {nombre_de_paires}")
print("Liste des pairs : ")
print(liste_paires)

def trier_dictionnaire_par_valeur(dico):
    dico_trie_par_value = dict(sorted(dico.items(), key=lambda item: item[1], reverse=True))
    return dico_trie_par_value

dico_trie_par_valeur = trier_dictionnaire_par_valeur(mon_dictionnaire)
print("\nDictionnaire trié par valeur (décroissant) :")
imprimer_dictionnaire(dico_trie_par_valeur)

# Création d'une fonction qui calcule la somme des n premiers nombres pairs 
def somme_des_n_premiers_even(n):
    total = 0
    num = 1
    while len(liste_paires) < n:
        if num % 2 == 0:
            total += num 
            liste_paires.append(num)
        num += 1
    return total

n = 50  
print(f"\nSomme des {n} premiers nombres pairs est : ")
print(somme_des_n_premiers_even(n))

# Calcul de la moyenne de tous les éléments du tableau 
moyenne = sum(random_numbers) / len(random_numbers)
print("\nMoyenne des nombres aléatoires générés :")
print(moyenne)

# Création d'une fonction qui trouve le nombre le plus élevé parmi une série de valeurs
def trouver_max(nombres):
    return max(nombres)

nombre_max = trouver_max(random_numbers)
print(f"\nLe nombre le plus élevé est : {nombre_max}")

