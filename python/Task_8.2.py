# 2) Создайте собственный класс-исключение, обрабатывающий ситуацию деления
# на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе
# пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.


class ZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    # код который может вызвать исключительную ситуацию
    num_1 = int(input("Введите делимое: "))
    num_2 = int(input("Введите делитель: "))
    if num_2 == 0:
        raise ZeroDiv("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число")
    # что делать если возникла исключительная ситуация
except ZeroDiv as err:
    print(err)
else:
    print(f"Частное от деления = {num_1 / num_2}")
    # что делать если ошибок не было
#finally:
    # выполняется всегда
