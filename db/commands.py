import json


def remove_commands(connection):
    """ Удаление таблицы """
    with connection.cursor() as cursor:
        cursor.execute("""DROP TABLE commands""")
        print("[DataBase] Table 'commands' has been removed")

def add_commands(connection):
    """ Добавление всех команд в таблицу (из json) """
    # Создание таблицы commands, если нет
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS commands (
                id serial PRIMARY KEY,
                command_type varchar(20) NOT NULL,
                command_name varchar(50) NOT NULL,
                command_description varchar(500) NOT NULL,
                command_use varchar(50) NOT NULL);"""
        )
        print("[DataBase] Table 'commands' created successful")

    # Получение json данных о командах
    with open("./../assets/commands.json", "r", encoding="utf-8") as jf:
        fd = json.load(jf)

    # Добавление команд в БД
    with connection.cursor() as cursor:
        for command in fd:
            cursor.execute(
                f"""INSERT INTO commands (command_type, command_name, command_description, command_use) VALUES
                ('{command["type"]}', '{command["name"]}', '{command["description"]}', '{command["use"]}');""")
        print("[DataBase] Table 'commands' has been changed")

def get_commands(connection, command):
    """ Получение данных о командах """
    with connection.cursor() as cursor:
        if command:
            cursor.execute("""SELECT * FROM commands WHERE command_name = %s""", (command,))
        else:
            cursor.execute("""SELECT command_type, command_name FROM commands""")
        return cursor.fetchall()
