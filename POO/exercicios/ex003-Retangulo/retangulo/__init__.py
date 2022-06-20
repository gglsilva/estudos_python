class Retangulo(object):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    
    def muda_valor_lados(self, base, altura):
        self.base = base
        self.altura = altura

    
    def retorna_valor_lados(self):
        return self.base, self.altura

    
    def calcula_area(self):
        return self.base * self.altura

    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
