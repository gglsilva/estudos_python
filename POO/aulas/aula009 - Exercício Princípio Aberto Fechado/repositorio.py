class Repositorio:
    
    def select(self, db_connection: any) -> str:
        conection = db_connection.conectar()
        print(f'Conectei ao banco {conection}')
        print('Fazendo um SELECT * FROM...')
        db_connection.desconectar()

    def insert(self, db_connection: any) -> str:
        conection = db_connection.conectar()
        print(f'Conectei ao banco {conection}')
        print('Fazendo um INSERT INTO...')
        db_connection.desconectar()
        