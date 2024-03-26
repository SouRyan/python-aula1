import math

n1= float(input("número real "))
absoluto= math.fabs(n1)
inteiro= math.trunc(n1)
raiz= math.sqrt(absoluto)
fatorial= round( math.factorial(inteiro), 2)
print(absoluto)
print(inteiro)
print(raiz)
print(fatorial)

