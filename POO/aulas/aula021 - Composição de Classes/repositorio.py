from sql_actions.insert import Insert
from sql_actions.select import Select


class Repositorio:
    
    def __init__(self) -> None:
        self.__insert = Insert() # instacia os objetos diretamente na classe
        self.__select = Select()
    
    def Select_by_id(self):
        self.__select.select_one()