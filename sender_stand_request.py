# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
# Это популярная библиотека, которая позволяет взаимодействовать с веб-сервисами
import requests 

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data 

#Этот код отправляет HTTP GET-запрос к заданному URL-адресу, который складывается 
#из базового адреса сервиса и пути к его документации, оба определены в модуле 
#конфигурации. Затем он выводит HTTP-статус код ответа от сервера, который указывает 
#на результат выполнения запроса.

# Определяем функцию get_docs, которая не принимает параметров
#request	Метод запроса
def get_docs():
    # Выполняем GET-запрос к URL, который складывается из базового URL-адреса сервиса
    # и пути к документации, заданных в модуле конфигурации
    # Функция возвращает объект ответа от сервера
    url = configuration.URL_SERVICE + configuration.DOC_PATH
    return requests.get(url)

# функция возвращает ответ с логами по умолчанию
def get_logs():
    # Складываем базовый URL из конфигурационного файла и путь к основным логам,
    # чтобы сформировать полный URL для запроса.
    # Возвращает объект ответа, полученный от сервера после выполнения GET-запроса
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count":20})

#функция возвращает ответ с данными из таблицы user.
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)



# Определение функции для отправки POST-запроса на поиск наборов по продуктам
def post_products_kits(products_ids):
    # Отправка POST-запроса с использованием URL из конфигурации, данных о продуктах и заголовков
    # Возвращается объект ответа, полученный от сервера
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids, # Тело запроса содержит ID продуктов в формате JSON 
                         headers=data.headers)  # Использование заголовков из файла data.py












