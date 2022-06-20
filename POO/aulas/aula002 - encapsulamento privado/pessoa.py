class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf    # __(underline) define um atribudo Privado em python

    def correr(self):
        print('Estou correndo...')

    def beber(self, bebida):
        if bebida == 'Cerveja':
            self.__apresentar_documento()
        else:
            print('Bebendo...')

    def __apresentar_documento(self):   # assim com atributos, basta acrescentar 2 underline na frente para definir um metodo privado
        print(self.__cpf)

ronaldo = Pessoa('Ronaldo Silva', 28, 90281938012908293)
#print(ronaldo.nome)
#print(ronaldo.idade)
# print(ronaldo.__cpf) se tentar printar irá levantar um erro
#ronaldo.print_cpf()     # atributos privados só podem ser assesados dentro do contexto da propria classe
ronaldo.beber('Cerveja')