"""
Funcoes nomeadas (padrões)

"""

def soma(x, y):
    """
    Funcao que soma dois valores 
    """
    return x+y


def div(x, y):
    '''
    Funcao que divide dois valores
    '''
    if x == 0 and y == 0:
        print('valores nao divisiveis')
    else:
        return x / y   
    

    


print(soma(2,3))
print(soma.__doc__)


print(div(0,0))
print(div.__doc__)
