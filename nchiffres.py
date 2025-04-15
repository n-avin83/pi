import time

def n_chiffres(n,f):
    start = time.time()

    with open(f, "r") as fichier:
        d = fichier.read()

    sequence = set()
    for i in range(len(d)-n+1):
        l = d[i:i+n]
        sequence.add(l)

        
    print(f"durée d'execution : {time.time() - start}")

    return len(sequence)

if __name__ == "__main__":
    n = int(input("n : "))
    f = input("fichier : ")

    print(n_chiffres(n,f))