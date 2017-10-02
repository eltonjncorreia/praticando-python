numero1 = int(input("Infome primeiro numero: "))
numero2 = int(input("Infome mais um numero: "))

if numero1 > numero2:
    print ("numero {} é o maior: ".format(numero1))
elif numero1 == numero2:
    print ("primeiro numero é {} e segundo é o numero {}, eles são iguais!".format(numero1,numero2))
else:
    print ("O segundo numero digitado é {}, e é o maior".format(numero2))
