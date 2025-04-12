import time
import gmpy2
from gmpy2 import mpz, get_context
from concurrent.futures import ProcessPoolExecutor
import sys

sys.set_int_max_str_digits(0)

def arctan_series(x, precision):
    """
    Calcule la série arctan(x) * scale_factor avec une précision donnée.
    On retourne un entier qui représente les décimales multipliées.
    """
    get_context().precision = precision * 4
    x = gmpy2.mpfr(1) / x
    x_power = x
    total = x
    x2 = x * x
    sign = -1
    k = 3

    while True:
        term = x_power / k
        if term == 0:
            break
        total += sign * term
        x_power *= x2
        k += 2
        sign *= -1

    return total


def calcule_pi_machin(D):
    """
    Calcule π en utilisant la formule de Machin avec D décimales.
    """
    # Définir la précision (plus grande que D pour éviter les erreurs d'arrondi)
    get_context().precision = D * 4
    scale_factor = gmpy2.pow(10, D)

    # Calculs parallélisés
    with ProcessPoolExecutor() as executor:
        future1 = executor.submit(arctan_series, 5, D)
        future2 = executor.submit(arctan_series, 239, D)
        arctan_1 = future1.result()
        arctan_2 = future2.result()

    pi = 4 * (4 * arctan_1 - arctan_2)
    return +pi


if __name__ == "__main__":
    D = 1_000_000  # nombre de décimales souhaitées
    start = time.time()

    # Calcul de π
    pi = calcule_pi_machin(D)

    # Sauvegarde en blocs
    with open("pi_machin.txt", "w") as f:
        pi_str = str(pi)
        for i in range(0, len(pi_str), 10000):
            f.write(pi_str[i:i+10000] + "\n")

    print(f"Temps total : {time.time() - start:.2f} secondes")
