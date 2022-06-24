from .interface import Repositorio

class MySqlRepositorio(Repositorio):

    def inserir(self, dado) -> None:
        print('Inserindo {} no Banco MySQL'.format(dado))

    def deletar(self, dado) -> None:
        print('Removendo {} no Banco MySQL'.format(dado))