# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 17:10:31 2025

@author: vinel
"""

import matplotlib.pyplot as plt
import math

def analyser_pi(nom_fichier="1 million de pi.txt"):
    print("Chargement des décimales...")
    try:
        with open(nom_fichier, "r") as f:
            content = f.read()
            # On nettoie pour ne garder que les chiffres (retrait du "3.")
            if "." in content:
                decimals = content.split(".")[1]
            else:
                decimals = content
    except FileNotFoundError:
        print(f"Erreur : Le fichier {nom_fichier} n'existe pas. Lance l'étape précédente !")
        return

    N_total = len(decimals)
    print(f"Analyse sur {N_total} décimales.")

    # --- 1. HISTOGRAMME DES CHIFFRES (ORDRE 1) ---
    counts = {str(d): 0 for d in range(10)}
    for d in decimals:
        counts[d] += 1
    
    frequences = [counts[str(d)] / N_total for d in range(10)]
    digits = list(range(10))

    plt.figure(figsize=(10, 5))
    plt.bar(digits, frequences, color='skyblue', edgecolor='black', alpha=0.7)
    plt.axhline(y=0.1, color='r', linestyle='--', label="Cible théorique (1/10)")
    plt.title(f"Répartition des chiffres de $\pi$ sur {N_total} décimales")
    plt.xlabel("Chiffre")
    plt.ylabel("Fréquence d'apparition")
    plt.ylim(0.09, 0.11) # Zoom pour voir les petites variations
    plt.xticks(digits)
    plt.legend()
    plt.grid(axis='y', alpha=0.5)
    plt.show()

    # --- 2. ÉTUDE DE LA CONVERGENCE (POINT FORT TIPE) ---
    # On veut montrer que l'erreur tend vers 0 quand N augmente
    print("Calcul de la convergence (cela peut prendre quelques secondes)...")
    
    steps = []
    errors = []
    
    # On prend des points de mesure logarithmiques pour aller vite
    # Ex: 100, 1000, 10000, 100000...
    max_log = int(math.log10(N_total))
    points_de_mesure = [int(10**(i/2)) for i in range(4, 2 * max_log + 1)] # Pas demi-entiers pour lisser
    
    for n in points_de_mesure:
        if n > N_total: break
        
        subset = decimals[:n]
        local_counts = {str(d): 0 for d in range(10)}
        for d in subset:
            local_counts[d] += 1
            
        # Calcul de l'écart moyen à la cible 0.1
        # Formule : Somme(|freq_obs - 0.1|)
        ecart_total = sum([abs(local_counts[str(d)]/n - 0.1) for d in range(10)])
        
        steps.append(n)
        errors.append(ecart_total)

    plt.figure(figsize=(10, 5))
    plt.loglog(steps, errors, marker='o', linestyle='-', color='purple')
    
    # Tracé d'une ligne de pente -1/2 (Loi des grands nombres / Tcl standard 1/sqrt(N))
    # Pour comparer la pente visuellement
    ref_x = steps
    ref_y = [1/math.sqrt(x) for x in ref_x] # Pente théorique typique
    plt.loglog(ref_x, ref_y, linestyle='--', color='gray', label="Pente théorique $1/\sqrt{N}$")

    plt.title("Convergence vers la distribution uniforme")
    plt.xlabel("Nombre de décimales $N$ (échelle log)")
    plt.ylabel("Erreur cumulée $\sum |f_{obs} - f_{th}|$ (échelle log)")
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()
    
    print("Analyse terminée.")

if __name__ == "__main__":
    analyser_pi()
