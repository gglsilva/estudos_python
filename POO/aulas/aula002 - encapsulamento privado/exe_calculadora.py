class Calculadora:

    def calcular(self, op, num1, num2):
        if op == '+':
            return self.__adicionar(num1, num2)
        elif op == '-':
            return self.__subtrair(num1, num2)
        else:
            print('Opção invalida')

    def __adicionar(self, num1, num2):
        return num1 + num2

    def __subtrair(self, num1, num2):
        return num1 - num2

calculadora = Calculadora()
print(calculadora.calcular('+', 4, 1))
print(calculadora.calcular('-', 6, 2))