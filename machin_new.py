from decimal import Decimal, getcontext
import math

def required_n(b, eps):
    """
    Calcule le rang n minimal tel que
    1 / ((2n+3) * b^(2n+3)) <= eps
    """
    n = 0
    while True:
        if Decimal(1) / ((2*n+3) * (Decimal(b) ** (2*n+3))) <= eps:
            return n
        n += 1

def machin_pi(D):
    # On garde un peu plus de chiffres pour éviter les erreurs d’arrondi
    getcontext().prec = D + 10
    
    # Paramètres Machin
    coeffs = [(4, 5), (-1, 239)]  # (c_i, b_i)
    sum_coeffs = sum(abs(c) for c, _ in coeffs)
    
    # Précision désirée
    eps_tot = Decimal(10) ** (-(D+1))
    eps_per = eps_tot / sum_coeffs
    
    # Calcul de chaque terme
    total = Decimal(0)
    for c, b in coeffs:
        n = required_n(b, eps_per)
        print(f"Pour arctan(1/{b}) : n = {n}")
        
        # Série d’arctan
        x = Decimal(1) / Decimal(b)
        term = x
        arct = Decimal(0)
        k = 0
        while k <= n:
            if k % 2 == 0:
                arct += term / (2*k+1)
            else:
                arct -= term / (2*k+1)
            term *= x*x
            k += 1
        
        total += c * arct
    
    # Formule Machin donne pi/4
    pi_approx = 4 * total
    
    # Arrondi final à D décimales
    getcontext().prec = D
    return +pi_approx  # le "+" force l’arrondi


# Exemple : calculer pi à 30 décimales
print(machin_pi(30))