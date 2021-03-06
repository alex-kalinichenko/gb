# 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

print('5 AND 6 =', 5 & 6, '<=>', bin(5), 'AND', bin(6), '=', bin(5 & 6))
print('Побитовое И (AND) используется для выключения битов. Любой бит, установленный\n'
      'в 0, вызывает установку соответствующего бита результата также в 0.\n')

print('5 OR 6 =', 5 | 6, '<=>', bin(5), 'OR', bin(6), '=', bin(5 | 6))
print('Побитовое ИЛИ (OR) используется для включения битов. Любой бит, установленный\n'
      'в 1, вызывает установку соответствующего бита результата также в 1.\n')

print('5 XOR 6 =', 5 ^ 6, '<=>', bin(5), 'XOR', bin(6), '=', bin(5 ^ 6))
print('Побитовое исключающее ИЛИ (XOR) устанавливает значение бита результата в 1,\n'
      'если значения в соответствующих битах исходных переменных различны.\n')

print(5 >> 2)  # сдвиг вправо на 2 знака - это деление на 4
print(5 << 2)  # свиг влево на 2 знака - это умножение на 4
