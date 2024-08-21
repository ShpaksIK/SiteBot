import psycopg2

from .commands import remove_commands, add_commands, get_commands


class Database:
    def __init__(self, host, user, password, dbname):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.connection = None

    def create_connection(self):
        """ Создание соединения c базой данных """
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                dbname=self.dbname
            )
            self.connection.autocommit = True

        except Exception as _ex:
            print("[DataBase] Error while working with PostgreSQL:", _ex)

    def close_connection(self, connection):
        """ Закрытие соединения с базой данных """
        if self.connection:
            self.connection.close()
            print("[DataBase] PostgreSQL connection closed")

    def get_version(self, connection):
        """ Получение версии базы данных """
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            print(f"[DataBase] {cursor.fetchone()}")

    def remove_commands(self, connection): return remove_commands(connection)
    def add_commands(self, connection): return add_commands(connection)
    def get_commands(self, connection, command=None): return get_commands(connection, command)