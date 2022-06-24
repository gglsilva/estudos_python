class Produto:

    def __init__(self,prod_nome, prod_valor) -> None:
        self.__prod_nome = prod_nome
        self.__prod_valor = prod_valor

    def informacoes_produto(self) -> None:
        print('Produto: {} / Valor: R$ {},00'.format(self.__prod_nome, self.__prod_valor))