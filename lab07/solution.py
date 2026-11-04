import numpy as np  # библиотека для работы с массивами: reshape, срезы, mean без циклов

# Плоский список измерений → таблица по width значений в строке
def reshape_rows(values, width):
    if width <= 0 or len(values) % width != 0:  # ширина некорректна или длина не делится нацело — форма не совпадает
        return []                                # по условию возвращаем пустой список
    data = np.asarray(values, dtype=float)      # плоский список → одномерный массив
    table = data.reshape(-1, width)             # меняем форму: -1 = «число строк посчитай сам», width значений в строке
    return np.round(table, 6).tolist()          # округляем весь массив сразу до 6 знаков → обычный список списков
