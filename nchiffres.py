from itertools import product
import time


def n_chiffres(n, f):
    start = time.time()
    chiffres = [str(i) for i in range(10)]

    fichier = open(f, "r")
    decimales = fichier.read()
    fichier.close()

    lst = []
    for i in range(len(decimales)-n+1):
        l = ""
        for j in range(n):
            l += str(decimales[i+j])
        lst.append(l)
    

    c= 0
    for elt in product(chiffres, repeat=n):
        e = ""
        for i in range(n):
            e += str(elt[i])
    
        if e in lst:
            c += 1


    print(time.time() - start)

    return c


print(n_chiffres(5, "carree.txt"))

