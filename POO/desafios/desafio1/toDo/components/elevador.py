from time import sleep

class Elevador:
    
    def __init__(self, andarAtual=1) -> None:
        self.__andarAtual = andarAtual
        self.andarMaximo = 15
        self.andarMinimo = 1

    def get_andar(self) -> int:
        return self.__andarAtual

    def set_andar(self, andar: int) -> None:
        self.__andarAtual = andar

    def transitar_andar(self, andar: int) -> None:
        if self.__andarAtual <= andar:
            subir = (andar - self.__andarAtual) 
            for num in range(subir):
                self.print_andar()
                self.__andarAtual = self.__andarAtual + 1
                sleep(1)
            self.print_andar()
        elif self.__andarAtual >= andar:
            descer = (self.__andarAtual - andar)
            for num in range(descer):
                self.print_andar()
                self.__andarAtual = self.__andarAtual - 1
                sleep(1)
            self.print_andar()  
    
    def print_andar(self) -> None:
        print('||=============||')
        print('||             ||')
        print('||             ||')
        print('||  Andar: {}  ||'.format(self.__andarAtual))
        print('||             ||')
        print('||             ||')
        print('||=============||')

