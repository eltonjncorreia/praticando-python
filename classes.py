from datetime import datetime as d


class Pessoa:

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def nome_completo(self):
        print('O nome é {}'.format(self._nome))

    def ano_nascimento(self):
        ano = d.today().year - self._idade
        print('Ano de nascimento é: {}'.format(ano))


