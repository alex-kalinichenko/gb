# 1) Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода
# реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность
# первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
# и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.

# вариант 2

import time


class TrafficLight:
    def __init__(self, __color):
        self.__color = __color

    def running(self):
        print("Traffic light: red")
        time.sleep(7)
        print("Traffic light: yellow")
        time.sleep(2)
        print("Traffic light: green")
        time.sleep(4)


while True:
    red_light = TrafficLight("Красный")
    red_light.running()
    yellow_light = TrafficLight("Жёлтый")
    yellow_light.running()
    green_light = TrafficLight("Зелёный")
    green_light.running()