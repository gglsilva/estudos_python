class Mae:

    def __init__(self) -> None:
        self.endereco = 'Rua dos Limoeiros'
        self.sobrenome = 'Silva'

    def comer(self) -> None:
        print('Estou comendo!!!')

    def estudar(self) -> None:
        print('Estou estudando!!!')


class Filha(Mae):

    def __init__(self) -> None:
        super().__init__() # chama o construtor da classe Mãe
        

clara = Filha()
clara.estudar() # Estou estudando!!! a ide