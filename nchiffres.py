import time
import csv

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
    nI = int(input("n init : "))
    nF = int(input("n final : "))

    en_tete = ["fichier","n chiffres","nb de sequences"]

    with open("n_chiffres.csv", "w") as fichier:
        writer = csv.writer(fichier, delimiter=",")
        writer.writerow(en_tete)

        for i in range(nI,nF+1):
            writer.writerow(["1 million de pi.txt",i, n_chiffres(i,"1 million de pi.txt")])
            writer.writerow(["carree_1M.txt",i, n_chiffres(i,"carree_1M.txt")])


