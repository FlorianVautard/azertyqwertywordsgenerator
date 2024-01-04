#!/bin/python
import requests
import random
import string

def obtenir_liste_de_mots(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.split('\n')
    else:
        print(f"Échec de récupération de la liste de mots. Code d'état : {response.status_code}")
        return []

def est_mot_valide(mot):
    return all(c.isalpha() or c.isspace() for c in mot)

def afficher_groupes_de_mots(mots, taille_groupe_defaut, nombre_groupes):
    taille_groupe = max(taille_groupe_defaut, 1)
    mots_valides = [mot for mot in mots if est_mot_valide(mot)]

    for i in range(nombre_groupes):
        groupe = random.sample(mots_valides, taille_groupe)
        print("".join(groupe))

if __name__ == "__main__":
    url_liste_mots = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    mots = obtenir_liste_de_mots(url_liste_mots)

    try:
        taille_groupe_defaut = int(input("Entrez le nombre de mots par groupe (par défaut est 4) : ") or 4)
        nombre_groupes = 20
    except ValueError:
        print("Entrée invalide. Utilisation de la taille de groupe par défaut, qui est 4.")
        taille_groupe_defaut = 4
        nombre_groupes = 20

    print(f"\nAffichage de {nombre_groupes} groupes de mots, chaque groupe contenant {taille_groupe_defaut} mots sans espace entre eux, sans caractères spéciaux :")
    afficher_groupes_de_mots(mots, taille_groupe_defaut, nombre_groupes)

