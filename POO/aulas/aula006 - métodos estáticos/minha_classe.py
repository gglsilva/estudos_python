class MinhaClasse:

    def __init__(self, estado) -> None:
        self.estado = estado

    @staticmethod
    def metodo_estatico():      # Atribui um certo contexto ao metodo, separado da classe em si
        # print(self.estado) ou cls.estado não funcionam, porque o metodo não reconhece o contexto da classe
        print('Estou no meu metodo estatico :D')

obj = MinhaClasse(True)
obj.metodo_estatico()