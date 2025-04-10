def longueur(f):

    fichier = open(f, "r")
    d = fichier.read()
    fichier.close()

    return len(d)