from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def __init__(self) -> None:
        self.atributo = 'Olá Mundo'

    def metodo (self, elemento: str) -> None:
        print(elemento)

    @abstractmethod     # Decorador para metodos abstratos
    def metodo_abstrato(self) -> None:
        pass
