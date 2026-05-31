import numpy as np
from collections import Counter
import scipy.stats as stats

def test_chi2_decimales(decimales_str, k=1):
    """
    Effectue le test d'adéquation du Chi-2 sur les décimales pour tester l'équirépartition.
    
    Paramètres:
    - decimales_str : chaîne de caractères contenant les décimales (ex: "1415926535...")
    - k : taille du bloc (1 pour les chiffres, 2 pour les paires, etc.)
    """
    
    # 1. Découpage en blocs non chevauchants
    # Ex pour k=2 : "141592" -> ["14", "15", "92"]
    blocs = [decimales_str[i:i+k] for i in range(0, len(decimales_str) - k + 1, k)]
    n_blocs = len(blocs)
    
    # 2. Paramètres théoriques
    nb_categories = 10**k  # Pour k=2, il y a 100 catégories (de 00 à 99)
    esperance = n_blocs / nb_categories  # Fréquence théorique espérée (E)
    
    # Vérification de la validité du test (Règle de Cochran)
    if esperance < 5:
        print("Attention : l'échantillon est trop petit pour un test du Chi-2 valide (Espérance < 5).")
        return None
        
    # 3. Comptage des fréquences observées (O)
    # On initialise un tableau de zéros pour garantir que les blocs non apparus soient comptés comme 0
    frequences_obs = np.zeros(nb_categories)
    comptage = Counter(blocs)
    
    for bloc, occurence in comptage.items():
        if len(bloc) == k and bloc.isdigit():
            index = int(bloc)  # Le bloc "14" va à l'index 14 du tableau
            frequences_obs[index] = occurence
            
    # 4. Calcul de la statistique du Chi-2 : Somme des (O - E)^2 / E
    chi2_stat = np.sum((frequences_obs - esperance)**2 / esperance)
    
    # 5. Calcul de la p-value
    ddl = nb_categories - 1  # Degrés de liberté
    p_value = 1 - stats.chi2.cdf(chi2_stat, ddl)
    
    # 6. Affichage des résultats
    print(f"--- RÉSULTATS DU TEST DU CHI-2 (Blocs de taille {k}) ---")
    print(f"Nombre total de blocs analysés : {n_blocs}")
    print(f"Catégories possibles : {nb_categories}")
    print(f"Fréquence théorique espérée (E) : {esperance:.2f}")
    print(f"Statistique du Chi-2 calculée : {chi2_stat:.4f}")
    print(f"P-value : {p_value:.4f}")
    
    # Interprétation au seuil de risque classique de 5%
    alpha = 0.05
    if p_value > alpha:
        print("\nConclusion : On ne peut pas rejeter H0. La répartition est considérée comme UNIFORME.")
    else:
        print("\nConclusion : On rejette H0. La répartition présente un biais significatif.")
        
    return chi2_stat, p_value

# ==========================================
# EXEMPLE D'UTILISATION
# ==========================================
if __name__ == "__main__":
    # Génération d'une fausse chaîne de décimales (ici, générée aléatoirement pour l'exemple)
    # Dans votre TIPE, vous lirez votre fichier texte contenant le million de décimales de Pi
    decimale_test = "".join(np.random.choice(list("0123456789"), 1000000))
    
    # Test sur les chiffres isolés (k=1)
    test_chi2_decimales(decimale_test, k=1)
    print("\n" + "="*50 + "\n")
    # Test sur les paires de chiffres (k=2)
    test_chi2_decimales(decimale_test, k=2)
