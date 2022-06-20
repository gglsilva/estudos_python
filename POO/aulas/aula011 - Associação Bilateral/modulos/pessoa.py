class Pessoa:

    def __init__(self, nome) -> None:
        self.__local = None
        self.__nome = nome

    def entrar_no_local(self, local) -> None:
        self.__local.acender_luz()

    def se_apresentar(self) -> None:
        print('Meu nome é {}'.format(self.__nome))

    def apresentar_local(self) -> None:
        endereco = self.__local.get_endereco()

    def set_local(self, local: any) -> None:
        self.__local = local

    def get_local(self) -> any:
        return self.__local