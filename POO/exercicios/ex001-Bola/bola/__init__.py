class Bola(object):
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.materal = material

    def mostra_cor(self):
        print(f'A cor da bola é {self.cor}')

    
    def muda_cor(self, nova_cor):
        self.cor = nova_cor
        self.mostra_cor()