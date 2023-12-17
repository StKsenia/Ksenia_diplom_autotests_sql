# Ксения Станкевич, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data


# Функция для создания заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)


# Функция получения заказа по его номеру(number_track)
def get_order(number_track):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={number_track}"
    response = requests.get(get_order_url)
    return response


# Автотест
def test_order():
    # создаем заказ
    response = create_order(data.order_body)
    # получаем номер заказа
    number_track = response.json()["track"]
    print("Заказ номер:", number_track, " создан.")

    order_response = get_order(response.json()["track"])

    # Проверяется, что код ответа равен 200
    assert order_response.status_code == 200, f"Код: {order_response.status_code}"
    order_data = order_response.json()

    print(order_data)
