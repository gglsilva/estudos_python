class Macaco(object):
    def __init__(self, nome, bucho=list()):
        self.nome = nome
        self.bucho = bucho

    
    def comer(self, alimento):
        self.bucho.append(alimento)

    
    def ver_bucho(self):
        print(f'o Macaco {self.nome} tem {len(self.bucho)} alimentos no bucho que São: ' )
        for a in self.bucho:
            print(a, end=', ')


    def digerir(self):
        pass
    