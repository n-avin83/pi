import gmpy2
from gmpy2 import mpz, mpfr, get_context, sqrt
import math
import time

# Constantes Chudnovsky
A = mpz(13591409)
B = mpz(545140134)
C3_OVER_24 = mpz(640320)**3 // 24

def bs(a, b):
    if b - a == 1:
        if a == 0:
            P = Q = mpz(1)
        else:
            k = mpz(a)
            P = (6*k - 5)*(2*k - 1)*(6*k - 1)
            Q = k**3 * C3_OVER_24
        T = P * (A + B * a)
        if a % 2:
            T = -T
        return (P, Q, T)
    else:
        m = (a + b) // 2
        P1, Q1, T1 = bs(a, m)
        P2, Q2, T2 = bs(m, b)
        return (P1 * P2, Q1 * Q2, Q2 * T1 + P1 * T2)

def compute_pi(digits):
    # On met assez de bits pour représenter tous les chiffres (log2(10) ≈ 3.32193)
    get_context().precision = int(digits * math.log2(10)) + 100

    terms = int(digits / math.log10(53360)) + 1
    P, Q, T = bs(0, terms)

    # C doit être de type mpfr pour préserver la précision
    C = mpfr(426880) * sqrt(mpfr(10005))

    pi = C * Q / T  # Tout est en mpfr maintenant
    return pi

def format_pi(pi, digits):
    # Multiplier par 10^digits pour décaler la virgule
    scaled_pi = gmpy2.floor(pi * gmpy2.pow(10, digits))
    s = scaled_pi.digits()

    # Remettre la virgule après 1 chiffre
    return s[0] + '.' + s[1:].ljust(digits, '0')


if __name__ == "__main__":
    digits = 100_000
    start = time.time()
    pi = compute_pi(digits)  # ou 20 si tu veux exploiter tous tes cœurs

    with open("pi_chudnovski.txt", "w") as f:
        f.write(str(pi))

    print(f"Temps total : {time.time() - start:.2f} secondes")