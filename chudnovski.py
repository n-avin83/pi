import time
import gmpy2
from gmpy2 import mpz, mpq, mpfr, fac, sqrt, get_context
import sys
sys.set_int_max_str_digits(0)

def chudnovsky_term(k):
    """Calcule le k-ième terme de la série de Chudnovsky."""
    # Constantes
    C = 426880 * sqrt(mpfr(10005))
    
    # Termes du numérateur et dénominateur
    numerator = mpz(fac(6*k)) * (545140134*k + 13591409)
    denominator = mpz(fac(3*k)) * (fac(k)**3) * (mpz(640320)**(3*k))

    return mpq(numerator, denominator)


def calcule_pi_chudnovsky(D):
    """Calcule π avec D décimales de précision grâce à la formule de Chudnovsky."""
    get_context().precision = D * 4  # sécurité
    total = mpq(0)
    k = 0

    # Combien de termes pour D décimales ? Environ D / 14
    max_k = D // 14 + 1

    for k in range(max_k):
        term = chudnovsky_term(k)
        if k % 2 == 1:
            total -= term
        else:
            total += term

    C = 426880 * sqrt(mpfr(10005))
    pi = C / total
    return +pi


if __name__ == "__main__":
    D = 1_000_000  # décimales souhaitées
    start = time.time()

    pi = calcule_pi_chudnovsky(D)

    # Sauvegarde efficace
    with open("pi_chudnovsky.txt", "w") as f:
        f.write(str(pi))

    print(f"Temps total : {time.time() - start:.2f} secondes")
