
lista_profissao = ['Medico', 'Programador']

for profissao in lista_profissao:
    print("* {}".format(profissao))

profissao = str(input("Informe qual a sua profissao baseado na lista acima: "))
salario = float(input("Qual o seu salario: "))


if profissao in lista_profissao:

    if 'Medico' == profissao:
        novo_salario =salario + (salario * (20/100))
        print("Teve aumento 20%, seu novo salario é: {}".format(novo_salario))

    elif 'Programador' == profissao:
        novo_salario =salario + (salario * (40/100))
        print("Teve aumento de 40%, seu novo salario é: {}".format(novo_salario))
else:
    print("Nova profissao")
