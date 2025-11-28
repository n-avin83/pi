import matplotlib.pyplot as plt
import numpy as np
from mpmath import mp

def visualiser_equirepartition_pi(n_iterations=2000):
    """
    Visualise l'orbite de Pi sous f(x) = {10x} pour montrer l'équirépartition.
    n_iterations : nombre de points à calculer (plus il est grand, plus c'est dense).
    """
    print(f"=== Calcul de {n_iterations} itérations sur π avec haute précision ===")
    
    # 1. Configuration de la précision (Indispensable pour les irrationnels)
    # On demande un peu plus de décimales que d'itérations pour éviter les erreurs de fin.
    mp.dps = n_iterations + 50  
    
    # On récupère pi avec la précision voulue
    # mp.pi est un objet "mpf" (multi-precision float)
    pi_val = mp.pi
    
    valeurs = []
    # On calcule les itérations : x_n = {10^n * pi}
    # Astuce : mpmath permet de faire ça proprement sans multiplier par 10^n (trop lourd)
    # Mais pour la simplicité de la boucle f(x) = {10x} :
    
    courant = pi_val
    
    # Boucle d'itération dynamique
    for i in range(n_iterations):
        # f(x) = partie fractionnaire de (10 * x)
        courant = (courant * 10) % 1
        valeurs.append(float(courant)) # On convertit en float juste pour le graphique
        
        if i % 500 == 0:
            print(f"Calcul : {i}/{n_iterations} itérations...")

    # 2. Création de la double visualisation
    fig = plt.figure(figsize=(14, 7))
    
    # --- Graphique 1 : Le Cercle Unité (Vue Topologique) ---
    ax1 = fig.add_subplot(121, projection='polar')
    
    # Conversion en angles (0 à 2pi)
    # On décale de pi/2 pour avoir le 0 (chiffre 0) en haut
    angles = [np.pi/2 - (2 * np.pi * v) for v in valeurs]
    rayons = [1.0] * len(valeurs) # Tous sur le cercle unité
    
    # On utilise un dégradé de couleur (colormap) pour montrer le temps qui passe
    # Bleu = début de l'orbite, Rouge = fin de l'orbite
    couleurs = range(len(valeurs))
    
    scatter = ax1.scatter(angles, rayons, c=couleurs, cmap='plasma', s=15, alpha=0.5, edgecolors='none')
    
    # Esthétique du cercle
    ax1.set_ylim(0, 1.1)
    ax1.set_yticklabels([]) # Enlever les rayons concentriques
    ax1.set_xticklabels([]) # On enlève les degrés pour mettre nos propres repères si besoin
    ax1.grid(False)
    
    # Ajouter le cercle limite
    ax1.plot(np.linspace(0, 2*np.pi, 100), [1]*100, color='black', linewidth=0.5)
    ax1.set_title(f"Orbite de $\pi$ sur le cercle unité\n($N={n_iterations}$ points)", fontsize=14)

    # --- Graphique 2 : L'Histogramme (Preuve de l'Uniformité) ---
    ax2 = fig.add_subplot(122)
    
    # On découpe l'intervalle [0, 1] en 10 classes (pour les chiffres 0-9) ou plus
    nb_classes = 10
    n, bins, patches = ax2.hist(valeurs, bins=nb_classes, range=(0, 1), 
                                color='skyblue', edgecolor='black', alpha=0.7)
    
    # Ligne cible théorique (Si c'est parfaitement équiréparti)
    cible = n_iterations / nb_classes
    ax2.axhline(cible, color='red', linestyle='--', linewidth=2, label='Distribution Uniforme Théorique')
    
    ax2.set_title("Histogramme de répartition des valeurs", fontsize=14)
    ax2.set_xlabel("Valeur dans [0, 1] (correspond aux décimales)", fontsize=12)
    ax2.set_ylabel("Fréquence d'apparition", fontsize=12)
    ax2.legend()
    
    # Calcul de l'écart type par rapport à l'uniformité (Indicateur de qualité)
    ecart_moyen = np.std(n)
    text_str = f"Cible idéale : {int(cible)}\nÉcart-type : {ecart_moyen:.2f}"
    ax2.text(0.05, 0.95, text_str, transform=ax2.transAxes, 
             fontsize=12, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

    plt.tight_layout()
    print("Affichage...")
    plt.show()

if __name__ == "__main__":
    # Tu peux augmenter n_iterations à 10000 pour voir l'histogramme s'aplatir parfaitement
    visualiser_equirepartition_pi(n_iterations=5000)
