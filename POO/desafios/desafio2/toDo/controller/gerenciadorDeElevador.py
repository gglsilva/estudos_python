class GerenciadorDeElevador():

    def __init__(self, elevador1, elevador2 ) -> None:
        self.__elevadores = [elevador1, elevador2]

    def transitar(self, id, andar) -> None:
        if (1 < andar > 15): return self.__msg_erro()
        else: return self.__filtrar_elevador(id, andar)

    def __filtrar_elevador(self, id, andar):
        for elevador in self.__elevadores:
            if elevador.get_id() == id:
                return self.__alterar_andar(andar, elevador)

        return self.__msg_erro()
            
    def __alterar_andar(self, andar, elevador):
        elevador.set_andar(andar)
        return self.__msg_sucesso(elevador)

    def __msg_sucesso(self, elevador):
        return f'Elevador {elevador.get_id()} indo para o {elevador.get_andar()}º andar'

    def __msg_erro(self) -> str:
        return 'Andar Invalido.'
