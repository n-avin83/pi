import time
from concurrent.futures import ProcessPoolExecutor
import sys
sys.set_int_max_str_digits(0)  # Permet de gérer de très grands entiers

def calcule_serie_1(D):
    """Calcule la première série : 16 * arctan(1/5)"""
    terme = 16 * 10**D // 5
    pi_approx = 0
    k = 0
    puissance = -25 
    while terme != 0:
        pi_approx += terme // (2 * k + 1)
        terme //= puissance
        k += 1
    return pi_approx

def calcule_serie_2(D):
    """Calcule la deuxième série : -4 * arctan(1/239)"""
    terme = -4 * 10**D // 239
    pi_approx = 0
    k = 0
    puissance = -239**2  
    while terme != 0:
        pi_approx += terme // (2 * k + 1)
        terme //= puissance
        k += 1
    return pi_approx

def calcule_pi(D):
    """Calcule D décimales de π en utilisant la formule de Machin"""
    start = time.time()
    with ProcessPoolExecutor() as executor:  # Remplace ThreadPoolExecutor par ProcessPoolExecutor
        # Parallélisation des deux séries
        result1 = executor.submit(calcule_serie_1, D)
        result2 = executor.submit(calcule_serie_2, D)
        pi_approx = result1.result() + result2.result()
    print(f"Temps d'exécution : {time.time() - start} secondes")
    return pi_approx

if __name__ == "__main__":
    # Nombre de décimales à calculer
    D = 1_000_000  # Par exemple, 1 million de décimales

    # Mesure du temps de démarrage
    start = time.time()

    # Calcul de π
    pi = calcule_pi(D)

    # Sauvegarde du résultat dans un fichier
    with open("pi_test.txt", "w") as fichier:
        fichier.write(str(pi))

    # Affichage du temps total d'exécution
    print(f"Temps total : {time.time() - start} secondes")