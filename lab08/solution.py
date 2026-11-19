import numpy as np

# Задание 1. Создание массивов

# arange(начало, стоп, шаг) — числа от 0 до 21 (22 не включается) с шагом 3
hours = np.arange(0, 22, 3)

# linspace(начало, конец, количество) — 5 равномерных чисел, конец включён
line = np.linspace(0, 1, 5)

# zeros — вектор нулей; dtype=int, чтобы были целые числа, а не дробные
zeros = np.zeros(6, dtype=int)

# full — матрица 2x3, заполненная значением -1
unknown_table = np.full((2, 3), -1)

# eye — единичная матрица: единицы на главной диагонали, нули вокруг
identity = np.eye(3, dtype=int)

print(hours)                    # сам массив
print(hours.shape)              # форма: (8,) — одномерный, 8 элементов
print(hours.ndim)               # число измерений: 1
print(hours.size)               # всего элементов: 8
print(hours.dtype)              # тип элементов: int64 (целые числа)

# Задание 2. Индексы и срезы вектора

print(hours[2])     # третий элемент (индексация с нуля!)
print(hours[-1])    # последний элемент: минус 1 = отсчёт с конца
print(hours[2:6])   # индексы 2, 3, 4, 5 — правая граница НЕ входит
print(hours[::2])   # каждый второй: шаг 2 (0, 2, 4, ...)
print(hours[::-1])  # шаг -1 разворачивает массив в обратный порядок

# Задание 3. Строки и столбцы таблицы

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

# У двумерного массива shape — это (строки, столбцы)
print(temperatures.shape)      # (3, 4)
print(temperatures.ndim)       # 2 измерения
print(temperatures.size)       # 3 * 4 = 12 элементов

print(temperatures[1, 2])      # элемент [строка 1, столбец 2] -> 16
print(temperatures[0])         # вся первая строка
print(temperatures[:, -1])     # последний столбец: «:» = все строки
print(temperatures[:2, 1:])    # строки 0-1, столбцы с 1 и до конца

# Два среза подряд дают прямоугольный фрагмент (строки 0-1, столбцы 1-2)
print(temperatures[:2, 1:3])

# Задание 4. Прямоугольные срезы матрицы 5x5

# arange(1, 26) — числа 1..25, reshape превращает вектор в матрицу 5x5
matrix = np.arange(1, 26).reshape(5, 5)

for fragment, title in [
    (matrix[:3, :],   'Первые три строки'),
    (matrix[-2:, :],  'Последние две строки'),
    (matrix[:, :2],   'Первые два столбца'),
    (matrix[1:4, 2:5], 'Строки 1-3, столбцы 2-4'),
    (matrix[-2:, -2:], 'Правый нижний блок 2x2'),
]:
    print(f'{title}:\n{fragment}\nshape: {fragment.shape}')

# Задание 5. Изменение массива через срезы

# copy() создаёт НЕЗАВИСИМУЮ копию. Срез без copy() возвращает только
# «вид» на те же данные: изменил бы changed_hours — изменился бы и hours.
changed_hours = hours.copy()
changed_hours[2:5] = 99   # индексы 2, 3, 4 — сразу весь диапазон
changed_hours[::2] = -1   # каждый второй, начиная с первого (0, 2, 4, ...)

print(changed_hours)
print(hours)              # исходный не пострадал — в этом смысл copy()

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0        # вся вторая строка
changed_matrix[:, -1] = -1      # весь последний столбец
changed_matrix[1:4, 1:4] = 100  # центральный блок 3x3 (индексы 1-3)

print(changed_matrix)
print(matrix)             # исходная matrix не изменилась

# Задание 6. Изменение формы

# reshape работает, только если новое произведение измерений равно
# числу элементов: 3 * 4 = 12 — верно, а 5 * 3 = 15 != 12 — будет ошибка.
numbers = np.arange(12)          # вектор из 12 чисел: 0..11
table = numbers.reshape(3, 4)    # матрица 3 строки x 4 столбца
transposed = table.T             # .T меняет строки и столбцы местами

print(numbers.shape)     # (12,)
print(table.shape)       # (3, 4)
print(transposed.shape)  # (4, 3)