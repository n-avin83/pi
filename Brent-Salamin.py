from decimal import Decimal, getcontext, localcontext

def calculer_pi_brent_salamin(ordre_precision):
    # On ajuste la précision du contexte (+5 pour éviter les erreurs d'arrondi à la fin)
    getcontext().prec = ordre_precision + 5
    
    # Initialisation des constantes sous forme d'objets Decimal
    un = Decimal(1)
    deux = Decimal(2)
    quatre = Decimal(4)
    
    a = un
    b = un / deux.sqrt()  # 1 / sqrt(2)
    t = un / quatre       # 1 / 4
    p = un
    
    # 20 itérations suffisent pour doubler la précision jusqu'à 1 000 000 de décimales
    for n in range(20):
        a_suivant = (a + b) / deux
        t = t - p * ((a - a_suivant) ** 2)
        b = (a * b).sqrt() # Utilise bien le 'a' de l'étape n
        a = a_suivant      # Met à jour 'a' pour l'étape n+1
        p = deux * p       # p_n+1 = 2 * p_n
        
    # Formule finale de Brent-Salamin
    pi = ((a + b) ** 2) / (quatre * t)
    
    # On tronque à la précision demandée par l'utilisateur
    return str(pi)[:-5]

# Exemple d'utilisation pour afficher les 50 premières décimales
print("Pi =", calculer_pi_brent_salamin(50))
