h= float(input("informe sua altura"))
genero =input("informe seu genero com M para masculino ou F para feminino ").upper()

if genero == 'M':
    pi1= ((72.7*h)-58)
    print("o peso ideal para a altura ", h, "é","{:.1f}".format(pi1) )
else:
    if genero == 'F':
        pi= float( (62.1*h)- 44.7)
        print(f'''o peso ideal para a altura {h}''' "é", "{:.1f}".format(pi))
    else:
        print("Genero invalido")