from decimal import Decimal, getcontext
import math
import time
import sys
sys.set_int_max_str_digits(0)

def chudnovski(d):
    getcontext().prec = d + 2
    C = 426880 * Decimal(math.sqrt(10005))
    K = Decimal(6*0)
    M = Decimal(1)
    X = Decimal(1)
    L = Decimal(13591409)
    S = L

    for k in range(1, d//14):
        K += 12
        M *= (K**3 - 16*K) / (k**3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X

    pi = C/S
    return str(pi)[:d + 2]


start = time.time()
fichier= open("pi_chudnovski.txt", "w")
fichier.write(str(chudnovski(1000000)))
fichier.close()
print(time.time() - start)
