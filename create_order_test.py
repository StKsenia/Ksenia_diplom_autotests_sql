# Ксения Станкевич, 11-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data


# Автотест
def test_order():
    # создаем заказ

    response = sender_stand_request.create_order(data.order_body)

    # получаем номер заказа
    number_track = response.json()["track"]
    print("Заказ номер:", number_track, " создан.")

    order_response = sender_stand_request.get_order(response.json()["track"])

    # Проверяется, что код ответа равен 200
    assert order_response.status_code == 200, f"Код: {order_response.status_code}"
    order_data = order_response.json()

    print(order_data)