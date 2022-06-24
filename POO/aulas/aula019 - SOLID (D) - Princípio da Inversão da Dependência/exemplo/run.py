from typing import Type
from db.mysql_repostory import MySqlRepositorio

class Usuario:

    def __init__(self, repositorio: Type[MySqlRepositorio]) -> None:
        self.__repositorio = repositorio
        
    def armazenar_dados(self, dado:any) -> None:
        self.__repositorio.inserir(dado)

    def remover_dados(self, dado:any) -> None:
        self.__repositorio.deletar(dado)

"""
Esse comportamento injeta a dependencia de MySqlRepositorio
na classe Usuario, fazendo com que a classe usuario seja completamente firme ao
mysqlRepositorio, se ouver a necessidade de implementar uma outra classe por exemplo
mongoRepositorio isso pode se torna um problema
"""
usario = Usuario(MySqlRepositorio())
usario.armazenar_dados(23)