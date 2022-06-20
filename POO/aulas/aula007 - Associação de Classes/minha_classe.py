from typing import Type

class Interruptor:

    def __init__(self, comodo: str) -> None:
        self.__comodo = comodo

    def acender(self) -> None:
        print(f'acendendo luz do comodo: {self.__comodo}')

    def apagar(self) -> None:
        print(f'apagando luz do comodo: {self.__comodo}')

    
class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    def dormir(self):
        print('fui dormir...')


lhama = Pessoa()
interruptor_quarto = Interruptor('quarto')

interruptor_quarto.acender()    # chamada direta para o metodo acender da classe interruptor
lhama.acender_luz(interruptor_quarto)   # toma o tipo de interruptor(interruptor_quarto no caso) para lhama executar a ação