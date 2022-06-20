from matplotlib.pyplot import table


class DatabaseConn:

    def __init__(self) -> None:
        self.__database = 'Postgres' # private
        self._conn = '//connection_string' # protected
        self.user = 'Lhama' # public

    def get_database(self) -> str:
        return self.__database

    def _testing_connection(self) -> None:
        print('Connection ok!...')

        
class Repository(DatabaseConn):

    def __init__(self) -> None:
        super().__init__()
        # print(self.user)
        # print(self.__database)
        # print(self._conn)

    def select(self) -> None:
        self._testing_connection()
        print('Connecting to {}...'.format(self._conn))
        print('SELECT * FROM table')
        print(self.user)


repo = Repository()
repo.select()