class Pessoa(object):
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura


    def envelhecer(self):
        self.idade += 1
        self.crescer()
    

    def engordar(self):
        self.peso += 1

    
    def emagrecer(self):
        self.peso -= 1
    

    def crescer(self):
        if self.idade < 21:
            self.altura += 0.05


    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}, Altura: {self.altura}cm'