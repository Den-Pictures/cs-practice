import numpy as np  # библиотека для работы с массивами: reshape, срезы, mean без циклов

# Плоский список измерений → таблица по width значений в строке
def reshape_rows(values, width):
    if width <= 0 or len(values) % width != 0:  # ширина некорректна или длина не делится нацело — форма не совпадает
        return []                                # по условию возвращаем пустой список
    data = np.asarray(values, dtype=float)      # плоский список → одномерный массив
    table = data.reshape(-1, width)             # меняем форму: -1 = «число строк посчитай сам», width значений в строке
    return np.round(table, 6).tolist()          # округляем весь массив сразу до 6 знаков → обычный список списков

# Участок таблицы: указанные строки и столбцы в заданном порядке
def block(matrix, rows, columns):
    if not matrix:                               # пустая таблица — пустой результат
        return []
    data = np.asarray(matrix, dtype=float)      # таблица → двумерный массив
    selected = data[np.ix_(rows, columns)]      # np.ix_: строки и столбцы «все со всеми» в указанном порядке
    return np.round(selected, 6).tolist()       # округляем сразу всё → обычный список

