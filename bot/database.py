import sqlite3 as sql


# Чтение данных пользователя из БД
def users_read(user_id):
    connectinon = sql.connect("database.db", check_same_thread=False)  # Соединение с БД

    # Преобразование списка в словарь
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    connectinon.row_factory = dict_factory
    cursor = connectinon.cursor()
    # Подготовить запрос в БД
    mySQLQuery = ('''
    SELECT *
    FROM users
    WHERE id = {}
    '''.format(user_id))
    cursor.execute(mySQLQuery)  # Выполнить запрос в БД
    results = cursor.fetchall()  # Результат из БД
    connectinon.close()  # Закрыть соединение с БД
    # Если данные есть, то выдать их, если нет, то вернуть None
    if len(results) != 0:
        return results[0]
    else:
        return None


# Регистрация пользователя в БД
def user_register(user_id, name, group):
    connectinon = sql.connect("database.db", check_same_thread=False)  # Соединение с БД
    cursor = connectinon.cursor()
    # Подготовить запрос в БД
    mySQLQuery = (f'''
        INSERT INTO users
        ('id', 'name', 'group', 'create_queue')
        VALUES ({user_id}, '{name}', '{group}', '')
        ''')
    cursor.execute(mySQLQuery)  # Выполнить запрос в БД
    connectinon.commit()  # Сохранить, занесённые изменения
    connectinon.close()  # Закрыть соединение с БД


# Сохранение данных у пользователя в БД
def users_save(user_id, choice='', value=None):
    connectinon = sql.connect("database.db", check_same_thread=False)  # Соединение с БД
    cursor = connectinon.cursor()
    # Подготовить запрос в БД
    mySQLQuery = (f'''
    UPDATE users 
    SET "{choice}"="{value}" 
    WHERE "id"= "{user_id}"
    ''')
    cursor.execute(mySQLQuery)  # Выполнить запрос в БД
    connectinon.commit()  # Сохранить, занесённые изменения
    connectinon.close()  # Закрыть соединение с БД
