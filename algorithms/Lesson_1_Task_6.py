# 8. Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого).

a = int(input('Введите 1-е число: '))
b = int(input('Введите 2-е число: '))
c = int(input('Введите 3-е число: '))

print('Среднее число =', a + b + c - max(a, b, c) - min(a, b, c))


