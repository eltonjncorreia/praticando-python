
nome = input("Qual o seu nome? ")

altura = float(input("Olá! {}, informe altura da parede? ".format(nome)))

comprimento = float(input("Qual o comprimento? "))

tinta_litros = float(input("quantos mêtros o galão de tinta pinta? "))

area = altura * comprimento

galao = int(area / tinta_litros)



if area <= tinta_litros:
    galao = 1
    print("Sua área é {:.2f} m² e você deve comprar {} galão de tinta ".format(area, galao))
else:
    print("Sua área é {:.2f} m² e você deve comprar {} galões de tinta ".format(area, galao))