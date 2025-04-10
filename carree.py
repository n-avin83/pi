import sys
sys.set_int_max_str_digits(0)


carree  = ""

for i in range(10000):
    carree += str(2**i)



fichier = open("carree.txt", "w")
fichier.write(carree)
fichier.close()