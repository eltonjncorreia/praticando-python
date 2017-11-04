import unittest


lista = []

def arm(num):
    if num not in lista:
        lista.append(num)
        print(num)
    return lista


class ArmazenarNum(unittest.TestCase):

    def test_armazenarNum(self):
        self.assertEqual(arm(4), lista)