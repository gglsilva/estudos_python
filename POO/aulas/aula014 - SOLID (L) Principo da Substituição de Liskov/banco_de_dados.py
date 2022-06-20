# exemplo mais pratico
from typing import Type

class Conexao:

    def conectar(self) -> None:
        print('Conectando...')

    def desconectar(self) -> None:
        print('Desconectando...')


class MysqlRepo(Conexao):

    def __init__(self) -> None:
        self.conexao = Conexao()

    def select(self):
        self.conectar()
        print('SELECT * FROM tabela')

class CasoDeUso:

    def buscar(self,db_repo: Type[MysqlRepo]):
        db_repo.select()