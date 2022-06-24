from typing import Type
#from db.mysql_repostory import MySqlRepositorio
from db.interface import Repositorio
from db.mongo_repository import MongoRepositorio
from db.mysql_repostory import MySqlRepositorio

class Usuario:

    def __init__(self, repositorio: Type[Repositorio]) -> None:
        self.__repositorio = repositorio
        
    def armazenar_dados(self, dado:any) -> None:
        self.__repositorio.inserir(dado)

    def remover_dados(self, dado:any) -> None:
        self.__repositorio.deletar(dado)

"""
Ao inves de usuario depender de MongoRepositorio ou mysqlRepositorio
ele irar depender da interface, isso é o principio da inversão de dependencia
e torna o projeto muito mais passivel de atualizações futuras 
"""

usario = Usuario(MySqlRepositorio())
usario.armazenar_dados(23)

usario2 = Usuario(MongoRepositorio())
usario2.armazenar_dados(23)