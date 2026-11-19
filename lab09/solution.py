import numpy as np

# Возвращает числа от 0 до 24
def make_hours() -> list[int]:
    return np.arange(0, 24, 3).tolist()

# Собирает отчёт по вектору: разные варианты индексации и срезов
def vector_report(values: list[float]) -> dict:
    arr = np.asarray(values, dtype=float)  # список - числовой массив
    return {
        "third": float(arr[2]), # третий элемент
        "last": float(arr[-1]), # последний
        "middle": arr[2:6].tolist(), # индексы от 2 до 5
        "every_second": arr[::2].tolist(), # каждый второй
        "reversed": arr[::-1].tolist(), # разворачивает массив
    }

# Возвращает изменённую копию: часть элементов заменяется без циклов
def change_vector(values: list[float]) -> list[float]:
    arr = np.asarray(values, dtype=float).copy() # copy чтобы не трогать исходник
    arr[2:5] = 99 # срезом заменяем индексы 2, 3, 4
    arr[::2] = -1 # каждый второй, начиная с первого (0, 2, 4, ...)
    return arr.tolist()

# Всё, что больше limit, обрезается до самого limit.
def cap_above(values: list[float], limit: float) -> list[float]:
    arr = np.asarray(values, dtype=float).copy()
    arr[arr > limit] = limit  # маска: заменяем сразу все элементы выше предела на предельное значение
    return arr.tolist()

# Перевод температур из Цельсия в Фаренгейты по формуле F = C * 9/5 + 32
def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    arr = np.asarray(values, dtype=float)
    return (arr * 9 / 5 + 32).tolist() # операция сразу над всем массивом