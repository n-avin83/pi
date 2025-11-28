# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 16:55:28 2025

@author: vinel
"""

import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction

def f(x):
    """Application f(x) = {10x} en arithmétique exacte"""
    return (10 * x) % 1

def visualiser_cycle_polaire(valeur_entree):
    print(f"=== Calcul du cycle pour {valeur_entree} ===")
    
    try:
        x0 = Fraction(valeur_entree)
    except ValueError:
        print("Erreur de format.")
        return

    # 1. Détection du cycle (Tortue et Lièvre simplifié par stockage)
    historique = []
    valeur_courante = x0
    
    # On itère jusqu'à retrouver une valeur déjà vue
    while valeur_courante not in historique:
        historique.append(valeur_courante)
        valeur_courante = f(valeur_courante)
        
        # Sécurité anti-boucle infinie (si jamais on met un irrationnel par erreur)
        if len(historique) > 1000:
            print("Cycle trop long ou non trouvé (irrationnel ?)")
            break
            
    # L'élément 'valeur_courante' est celui qui boucle.
    # On identifie où le cycle commence (pré-période vs période)
    try:
        debut_cycle = historique.index(valeur_courante)
        cycle = historique[debut_cycle:]
        pre_periode = historique[:debut_cycle]
        
        print(f"Longueur du cycle : {len(cycle)}")
        print(f"Cycle détecté : {[float(v) for v in cycle]}")
    except ValueError:
        print("Pas de cycle détecté dans la limite des itérations.")
        return

    # 2. Préparation du tracé (Coordonnées Polaires)
    # On map l'intervalle [0, 1] sur un angle [0, 2pi]
    # 0 est en haut (pi/2), et on tourne dans le sens horaire pour faire "horloge"
    def get_coords(val_frac):
        val_float = float(val_frac)
        angle = np.pi/2 - (2 * np.pi * val_float) # Rotation pour avoir 0 en haut
        return np.cos(angle), np.sin(angle)

    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Dessiner le cercle unité (le "fond")
    cercle = plt.Circle((0, 0), 1, color='#dddddd', fill=False, linestyle='--')
    ax.add_artist(cercle)

    # Tracer tous les points du cycle
    points_x = []
    points_y = []
    for val in cycle:
        x, y = get_coords(val)
        points_x.append(x)
        points_y.append(y)
        
        # Afficher la valeur décimale à côté du point
        # (On décale légèrement le texte pour ne pas être sur le point)
        ax.text(x*1.15, y*1.15, f"{float(val):.2f}", ha='center', va='center', fontsize=9)

    # Tracer les flèches (La boucle !)
    # On relie chaque point i au point i+1
    # Et on relie le dernier au premier pour fermer la boucle
    
    # On ajoute le premier point à la fin pour fermer la boucle visuellement
    points_x_plot = points_x + [points_x[0]]
    points_y_plot = points_y + [points_y[0]]

    for i in range(len(points_x)):
        start_x, start_y = points_x[i], points_y[i]
        end_x, end_y = points_x_plot[i+1], points_y_plot[i+1]
        
        ax.annotate("", xy=(end_x, end_y), xytext=(start_x, start_y),
                    arrowprops=dict(arrowstyle="->", color="blue", lw=2))

    # Tracer les points
    ax.scatter(points_x, points_y, color='red', zorder=10, s=100, label='États du cycle')

    # Esthétique
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.set_aspect('equal')
    ax.axis('off') # On cache les axes X/Y carrés
    plt.title(f"Visualisation du Cycle pour $x_0 = {valeur_entree}$\n(Représentation sur le cercle unité $\mathbb{{R}}/\mathbb{{Z}}$)", fontsize=14)
    
    plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    # Teste avec 1/7 (cycle parfait) ou 1/14 (pré-période puis cycle)
    input_str = input("Entrez une fraction (ex: 1/7) : ")
    visualiser_cycle_polaire(input_str)
