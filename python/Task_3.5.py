# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.

summ = 0
el = None
while True:
    user_input = input("Введите числа разделённые пробелом.\n"
                       "При нажатии Enter будет выведена сумма.\n"
                       "При нажатии 'q' програма завершит работу: ")
    if user_input in ['q', 'Q', 'й', 'Й']:
        break
    try:
        for el in user_input.split():
            if el in ['q', 'Q', 'й', 'Й']:
                break
            else:
                summ += int(el)
        print("Сумма введённых чисел = ", summ)
        if el in ['q', 'Q', 'й', 'Й']:
            break
    except ValueError:
        print("Введены некорректные значения.")
