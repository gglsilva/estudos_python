class MysqlDB:
    
    def __init__(self) -> None:
        self.__conexao = 'MysqlDB'

    def conectar(self) -> str:
        print('Conectando ao banco de dados: {}'.format(self.__conexao))
        return self.__conexao

    def desconectar(self) -> str:
        print('Desconectando do banco de dados: {}'.format(self.__conexao))
        