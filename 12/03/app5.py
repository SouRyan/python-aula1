peso=float( input("informe o peso em quilos do peixe"))

if peso >=50:
    excesso= float(peso/50)
    multa = 4*excesso
    print("sua multa é de", multa)
else:
    print("não prescisa pagar multa")

