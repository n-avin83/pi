# -*- coding: utf-8 -*-
import time
import sys
sys.set_int_max_str_digits(0)

global start


def calcule_pi(D):
    """Renvoie le calcul de D decimales de pi en utilisant la formule de machin"""

    
    
    
    pi_approx = 0
    
    #première serie pour 16*arctan(1/5)
    terme = 16* 10**D // 5
    k=0
    while terme != 0:
        pi_approx += terme // (2*k + 1)
        terme //= -25
        k+=1
        
    #deuxième serie pur -4*arctan(1/239)
    terme = -4*10**D//239
    k=0
    while terme != 0:
        pi_approx += terme // (2*k +1)
        terme //= -239**2
        k+=1
        
    print(time.time() - start)
    return pi_approx


start = time.time()
fichier= open("pi_doc.txt", "w")
fichier.write(str(calcule_pi(1000000)))
fichier.close()
print(time.time() - start)

