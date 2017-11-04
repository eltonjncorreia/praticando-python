genero_digitado = str(input("informe qual genero, digite apenas a primeira letra: "))

genero = genero_digitado.upper()

if "M" == genero:
    print("Masculino!")
elif "F" == genero:
    print("Feminino!")
else:
    print("Genero invalido!")