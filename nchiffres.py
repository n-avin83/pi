import time

def n_chiffres(n,f):
    start = time.time()

    fichier = open(f, "r")
    d = fichier.read()
    fichier.close()

    lst = []
    for i in range(len(d)-n+1):
        l = ""
        for j in range(n):
            l += str(d[i+j])
        if not l in lst:
            print(l)
            lst.append(l)

        
    print(f"durée d'execution : {time.time() - start}")

    return len(lst)


n = int(input("n : "))
f = input("fichier : ")

print(n_chiffres(n,f))