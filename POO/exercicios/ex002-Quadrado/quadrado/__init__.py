class Quadrado(object):
    def __init__(self, lado):
        self.lado = lado


    def muda_valo_lado(self, lado):
        self.lado = lado
        print(f'O NOVO valor do lado é {self.lado}')


    def retorna_valor_lado(self):
        print(f'O valor do lado é {self.lado}')


    def calcula_area(self):
        print(f'a area do quadrado é igual: {self.lado ** 2}')
        