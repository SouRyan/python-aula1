n1=float(input("coloque o primeiro número"))
n2=float(input("coloque o segundo número"))
n3=float(input("colque o terceiro número"))
if n1 == n2 ==n3:
    print("Os números inseridos são iguais ", n1)
else:
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
        print("O maior número é", maior)
