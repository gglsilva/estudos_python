class Casa:

    def __init__(self) -> None:
        self.__endereco = 'Rua dos Limoeiros'

    def acender_luzes(self) -> None:
        print('Estou acendendo as Luzes')

    def get_endereco(self) -> str:
        return self.__endereco


class Pessoa:

    def __init__(self, nome: str) -> None:
        self.__nome = nome

    def entrar_no_local(self, local: any) -> None:
        local.acender_luzes()

    def apresentar_local(self, local: any) -> None:
        endereco = local.get_endereco()
        print(f'O local é {endereco}')

casa_de_amigo = Casa()
ana = Pessoa('Ana')

ana.apresentar_local(casa_de_amigo)
ana.entrar_no_local(casa_de_amigo)
     