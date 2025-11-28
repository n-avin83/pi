# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 17:45:49 2025

@author: vinel
"""

import math

def charger_pi(nom_fichier="1 million de pi.txt"):
    """Charge les décimales depuis le fichier texte."""
    try:
        with open(nom_fichier, "r") as f:
            content = f.read()
            # On nettoie pour ne garder que les décimales pures
            if "." in content:
                decimals = content.split(".")[1]
            else:
                decimals = content
            return decimals
    except FileNotFoundError:
        print(f"Erreur : Impossible de trouver '{nom_fichier}'.")
        print("Lance d'abord le programme de génération (étape 1) !")
        return None

def estimer_probabilite(longueur_sequence, nb_decimales):
    """
    Estime la probabilité théorique de trouver une séquence de longueur k
    dans N décimales (Loi géométrique / Bernoulli).
    P = 1 - (1 - 1/10^k)^N
    """
    proba = 1 - math.exp(-nb_decimales / (10**longueur_sequence))
    return proba

def rechercher_sequence():
    print("=== Recherche de Motifs dans Pi ===")
    
    pi_str = charger_pi()
    if pi_str is None: return

    N = len(pi_str)
    print(f"Données chargées : {N} décimales disponibles.")

    while True:
        print("\n------------------------------------------------")
        target = input("Entrez une séquence (ex: 14072004 pour une date, ou 'q' pour quitter) : ")
        
        if target.lower() == 'q':
            break
            
        if not target.isdigit():
            print("Veuillez entrer uniquement des chiffres.")
            continue

        # 1. Calcul théorique
        proba = estimer_probabilite(len(target), N)
        print(f"-> Probabilité théorique de la trouver : {proba:.2%}")

        # 2. Recherche
        index = pi_str.find(target)

        if index != -1:
            # Trouvé !
            print(f"\n[SUCCÈS] Séquence trouvée à la position : {index + 1}")
            # Affichage du contexte (5 chiffres avant, 5 après)
            start = max(0, index - 5)
            end = min(N, index + len(target) + 5)
            
            contexte_avant = pi_str[start:index]
            contexte_seq = target
            contexte_apres = pi_str[index+len(target):end]
            
            print(f"Contexte : ... {contexte_avant} [{contexte_seq}] {contexte_apres} ...")
        else:
            # Pas trouvé
            print(f"\n[ÉCHEC] Séquence non trouvée dans les {N} premières décimales.")
            if len(target) >= 6 and N < 10000000:
                print("Conseil : Pour une date complète (8 chiffres), il faut souvent > 100 millions de décimales.")
                print("Essayez le format court (JJMMYY) ou juste (JJMM).")

if __name__ == "__main__":
    rechercher_sequence()
