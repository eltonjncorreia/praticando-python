# n1= int(input("informe a primeira nota"))
# n2= int(input("informe a segunda nota"))
# n3= int(input("informe a terceira nota"))
# n4= int(input("informe a quarta nota"))

# media = (n1+n2+n3+n4 / 4)
# print("sua media é {}".format(media))

# Refactoring
list_n = []
qt_notas = int(input("Informe quantas notas quer avaliar"))
while len(list_n) < qt_notas:
    list_n.append(int(input("Informe {} nota: ".format(len(list_n)+1))))

media = (sum(list_n)/qt_notas)
print("sua media é {}".format(media))