# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.


def dividing():
    try:
        num1 = int(input("Введите делимое: "))
        num2 = int(input("Введите делитель: "))
        num3 = num1 / num2
    except ZeroDivisionError:
        return "Ошибка: деление на ноль запрещено"
    except ValueError:
        return "Ошибка: некорректные значения"
    return num3


print(dividing())
