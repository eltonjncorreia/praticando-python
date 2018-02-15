

# Funcoes lambdas ou Anonimas
'''
Soma dois valores, funcao lambda
segundo a PEP 8 nomear funcoes lambda nao e uma boa pratica
'''
soma_lambda = lambda x, y: x + y


print(soma_lambda(2,2))

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(filter(lambda x: x % 3 == 0, foo))