import numpy as np

# Список измерений - таблица по width значений в строке
def reshape_rows(values, width): # значения, ширина строки
    if width <= 0 or len(values) % width != 0: # если ширина строки <= 0 или не делится нацело
        return []
    data = np.asarray(values, dtype=float) # список - одномерный массив
    table = data.reshape(-1, width) # преобразуем в матрицу
    return np.round(table, 6).tolist() # округляем каждый элемент матрицы и переводим в список списков

# Участок таблицы
def block(matrix, rows, columns):
    if not matrix:
        return []
    data = np.asarray(matrix, dtype=float) # матрица (таблица) - двумерный массив
    selected = data[np.ix_(rows, columns)] # делаем срез массива по указанным вводным параметрам
    return np.round(selected, 6).tolist() # округляем каждый элемент и преобразуем в список

# Среднее по каждому столбцу
def column_means(matrix):
    if not matrix:
        return []
    data = np.asarray(matrix, dtype=float) # матрица - двумерный массив
    means = data.mean(axis=0) # берём среднее значение по столбцу (1 - строки)
    return np.round(means, 6).tolist() # округляем каждый элемент и преобразуем в список

# Размах столбца
def column_range(matrix, column):
    if not matrix:
        return 0.0
    data = np.asarray(matrix, dtype=float) # матрица - двумерный массив
    values = data[:, column] # вырезаем все элементы какого-то столбца
    return round(values.max() - values.min(), 6)