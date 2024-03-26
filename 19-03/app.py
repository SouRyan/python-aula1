horas=float(input("Quanto você ganha por Hora?"))
mes=int(input("Quanto horas você trabalha por mês?"))
bruto= horas * mes
print('sua renda bruta é {}'.format(bruto))
impoRenda=(11*bruto)/100
inss=(8*bruto)/100
sindicato=(5*bruto)/100
print(impoRenda)
print(inss)
print(sindicato)
liquido=bruto-(impoRenda+inss+sindicato)
print("R$",liquido)