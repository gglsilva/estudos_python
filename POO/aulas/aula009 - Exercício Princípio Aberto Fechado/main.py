from repositorio import Repositorio
from databases import PostgresDB, MysqlDB

db_conn_postgres = PostgresDB()
db_conn_mysql = MysqlDB()

repo = Repositorio()
repo2 = Repositorio()

repo.insert(db_conn_postgres)
print('\n')
repo2.insert(db_conn_mysql)

