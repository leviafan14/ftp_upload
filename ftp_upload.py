import ftplib


def upload_to_ftp_server(server: str, username: str, password: str, file: str):
	# Авторизируемся на сервере
	session = ftplib.FTP(server, username, password)
	session.encoding = 'utf-8'
	# Указываем файл для загрузки на FTP сервер, открываем его на чтение как бинарный
	file_to_upload = open(file, 'rb')
	# Загружаем файл
	try:
		session.storlines(f'STOR {file_to_upload.name}', file_to_upload)
	except Exception as e:
		print(f'Не удалось загрузить файл на сервер {e}')
	finally:
		# Закрываем файл
		file_to_upload.close()
		# Завершаем сессию
		session.quit()
