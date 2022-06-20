class Alarme:

    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def get_estado(self) -> bool:
        return self.__estado

    #def set_estado(self, valor) -> bool:
    #    return self.__estado == valor

    def set_estado(self, valor: bool) -> None:
        if isinstance(valor, bool):     # Garante que o valor passado é do mesmo tipo que o desejado
            self.__estado = valor
        