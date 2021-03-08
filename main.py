# -*- coding: utf-8 -*-
from auth_data import *
from ftp_upload import *
from python_without_insert import *


if __name__ == "__main__":
	# Ввод данных для поиска через запятую
	user_name = []
	user_name = list(input('Введите фамилии через запятую: ').split(','))
	# Символ разделитель
	split_char = ":"
	# Вызов функции для получения данных из БД и записи в файл
	file = read_to_database(user_name, split_char)
	# Загрузка файла на FTP сервер
	upload_to_ftp_server(server, username, password, file)
