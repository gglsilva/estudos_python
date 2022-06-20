from abs_class import AbstractClass

class Filha(AbstractClass):

    def apresentar_metodo(self) -> None:
        print(self.atributo)

    # A classe filha é obrigada a implementar umo 
    # metodo abstrato
    def metodo_abstrato(self) -> None:
        print('Implementando metodo abstrato')

filha = Filha()
filha.apresentar_metodo()
filha.metodo('Estou aqui')

# Erro: classes abstratos não podem ter instancias
#AbstractClass = AbstractClass()
#abstractClass.metodo('Fazendo algo')