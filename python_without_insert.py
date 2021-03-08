import pymysql
from pymysql.cursors import DictCursor


def read_to_database(user_name: list, split_char: str) -> str:
    # Создаем подключение и проверяем удалось ли подключиться
    try:
        # Т.к. сервер локальный, то учетные данные передается напрямую в connection
        connection = pymysql.connect(
        host='localhost',
        user='root',
        password='admin',
        db='users',
        charset='utf8',
        cursorclass=DictCursor,
        use_unicode=True
        )
    except Exception as e:
        print(e)

    # Посик в списке пробелов (пустых элементов) и проверка списка на пустоту
    # Удаление пробелов из элементов списка
    user_name = list(map(str.strip, user_name))
    # Удаляем пустые элементы из списка
    user_name = [i for i in user_name if i != '']
    # Если список пустой, то выводится сообщение об этом
    if user_name is None:
        print(f'Lists is empty {user_name} ')
    else:
        pass
    # Создаем файл и открываем его для записи
    file_name = user_name[0]+'-'+user_name[-1]+".txt"
    file = open(file_name, "w")
    file.close()

    # Берем элементы из списка user_name и
    # Обращаемся к подключению которое создали
    for i in user_name:
            with connection.cursor() as cursor:
            # Запрос на чтение из БД
                select_query = 'SELECT account,name FROM users.users_data WHERE users.users_data.name=%s'
            # Получаем данные
                try:
                    cursor.execute(select_query,i)
                    print(i)
                except Exception as e:
                    print('Не удалось выполнить запрос в базу данных /n', e)
                    exit()
            # Вывод на экран
                for row in cursor:
                # Если данные есть, то выводим на экран и записываем в файл
                    if row['name'] is not None:
                        print(f"{row['account']} {row['name']}")
                    # Открываем файл для дозаписи
                        file = open(file_name, "a", encoding='utf-8')
                        file.write(str(row['account']).strip()+split_char+str(row['name']).strip()+'\n')
                        result = True
                    else:
                        pass
                try:
                    result
                except NameError as e:
                    print('Данные не получены, файл с результатами запроса не создан')

    # Закрываем файл и соединение
    file.close()
    connection.close()
    # Функция возвращяет имя файла
    return file.name
