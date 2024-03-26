nota1= float(input("digite a nota 1 "))
nota2= float(input("digite a nota 2 "))
resultado= (nota1+nota2)/2
if resultado <7:
    print("vc foi reprovado")
elif resultado == 10:
    print("aprovado por Distinção")
else:
    print("vc foi aprovado")