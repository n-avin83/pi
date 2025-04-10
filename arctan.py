from decimal import Decimal, getcontext
import sys
sys.set_int_max_str_digits(0)
getcontext().prec = 1000000

s= Decimal(0)

for i in range(1000000):
    s += Decimal((-1)**i)/Decimal(2*i+1)

s = Decimal(4)*s

fichier = open("pi_arctan.txt","w")
fichier.write(str(s))
fichier.close()