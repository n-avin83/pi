import gmpy2
from gmpy2 import mpz, mpfr, get_context, sqrt
from multiprocessing import Pool, cpu_count
import math
import time
import sys
sys.set_int_max_str_digits(0)

A = mpz(13591409)
B = mpz(545140134)
C3_OVER_24 = mpz(640320)**3 // 24

# Binary splitting sur un intervalle [a, b)
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

# Wrapper pour multiprocessing
def bs_wrapper(args):
    return bs(*args)

# Combinaison des résultats binaires
def merge_results(results):
    while len(results) > 1:
        new_results = []
        for i in range(0, len(results), 2):
            if i + 1 < len(results):
                P1, Q1, T1 = results[i]
                P2, Q2, T2 = results[i+1]
                new_results.append((P1 * P2, Q1 * Q2, Q2 * T1 + P1 * T2))
            else:
                new_results.append(results[i])
        results = new_results
    return results[0]

def compute_pi_parallel(digits, num_workers=None):
    if num_workers is None:
        num_workers = cpu_count()

    get_context().precision = int(digits * math.log2(10)) + 100
    terms = int(digits / math.log10(53360)) + 1

    # Diviser en blocs
    chunk_size = (terms + num_workers - 1) // num_workers
    ranges = [(i, min(i + chunk_size, terms)) for i in range(0, terms, chunk_size)]

    with Pool(num_workers) as pool:
        partial_results = pool.map(bs_wrapper, ranges)

    P, Q, T = merge_results(partial_results)

    C = mpfr(426880) * sqrt(mpfr(10005))
    pi = pi = C * mpfr(Q) / mpfr(T)
    return pi


if __name__ == "__main__":
    digits = 1_000_000
    start = time.time()
    
    pi = compute_pi_parallel(digits, 16)  # ou 20 si tu veux exploiter tous tes cœurs

    with open("pi_chudnovski.txt", "w") as f:
        f.write(str(pi))

    print(f"Temps total : {time.time() - start:.2f} secondes")