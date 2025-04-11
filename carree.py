import sys
sys.set_int_max_str_digits(0)


carree  = "1"
c=1
for i in range(1000000):
    c = c * 2
    carree += str(c)



fichier = open("carree.txt", "w")
fichier.write(carree)
fichier.close()