

def test(f):


    fichier = open("1 million de pi.txt", "r")
    pi = fichier.read()
    fichier.close()

    file = open(f, "r")
    pi_test = file.read()
    file.close()

    c= 0
    for i in range(min(len(pi), len(pi_test))):
        if pi[i] != pi_test[i]:
            c += 1

    return c



if __name__ == "__main__":
    # Test de la fonction
    f = "pi_chudnovski.txt"
    erreur = test(f)
    print(f"Nombre d'erreurs : {erreur}")

    