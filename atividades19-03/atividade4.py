
letra = input("coloque uma letra ").upper()
if letra in 'AEIOU' :
    print("é uma vogal")
elif letra in '1234567890':
        print("É um número")
else:
    print("é uma consoante")

