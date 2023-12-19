# Ксения Станкевич, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests


# Функция для создания заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)


# Функция получения заказа по его номеру(number_track)
def get_order(number_track):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={number_track}"
    response = requests.get(get_order_url)
    return response

