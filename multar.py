velocidade=int(input("Informe o valor da velocidade:"))

if velocidade >= 100:
    aumentar_valor=(velocidade-100)*5
    print("voce foi multado!")
    print("O valor de multa a pagar é : {}".format(aumentar_valor))
else:
    print("Parabens! Dirija com segurança, sua velocidade é: {}".format(velocidade))