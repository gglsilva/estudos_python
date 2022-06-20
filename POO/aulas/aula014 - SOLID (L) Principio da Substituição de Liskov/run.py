# Quebra do principo da substituição de Liskov
class PessoaA:

    def se_apresentar(self):
        print('Eu sou uma pessoa A')


class PessoaB(PessoaA):

    def __init__(self) -> None:
        super().__init__()

    def se_apresentar(self):
        print('Estou alterando esse metodo')

pessoa = PessoaA()
pessoa.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()