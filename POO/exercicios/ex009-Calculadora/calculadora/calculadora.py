class Calculadora:

    def calcular(self, operacao: str, num1: int, num2: int) -> int:
        if operacao == '+':
            return self.__adicionar(num1, num2)
        elif operacao == '-':
            return self.__subtrair(num1, num2)
        elif operacao == '*':
            return self.__multiplicar(num1, num2)
        elif operacao == '/':
            return self.__dividir(num1, num2)

    def __adicionar(self, num1: int, num2: int) -> int:
        return num1 + num2

    def __subtrair(self, num1: int, num2: int) -> int:
        return num1 - num2
    
    def __multiplicar(self, num1: int, num2: int) -> int:
        return num1 * num2
    
    def __dividir(self, num1: int, num2: int) -> int:
        return num1 / num2


calc = Calculadora()
print(calc.calcular('+', 10, 5))
print(calc.calcular('-', 10, 5))
print(calc.calcular('*', 10, 5))
print(calc.calcular('/', 10, 5))