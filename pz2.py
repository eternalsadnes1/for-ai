print("Задание 1\n")
import numpy as np

random_array_1d = np.random.randint(1, 101, size=10)
print(f"Случайный массив: {random_array_1d}")

sum_val = random_array_1d.sum()
mean_val = random_array_1d.mean()
prod_val = random_array_1d.prod()

print(f"Сумма элементов: {sum_val}")
print(f"Среднее значение: {mean_val}")
print(f"Произведение элементов: {prod_val}")

random_array_2d = np.random.rand(4, 5)
print("Двумерный массив 4x5:\n", random_array_2d)

max_in_rows = random_array_2d.max(axis=1)
min_in_rows = random_array_2d.min(axis=1)
min_indices_in_rows = random_array_2d.argmin(axis=1)

print("\nМаксимальные элементы в каждой строке:", max_in_rows)
print("Минимальные элементы в каждой строке:", min_in_rows)
print("Индексы минимальных элементов в каждой строке:", min_indices_in_rows) 

ones_array = np.ones((3, 3))
print("Массив из единиц:\n", ones_array)

random_array_3x3 = np.random.rand(3, 3)
print("\nСлучайный массив:\n", random_array_3x3)

result_array = ones_array + random_array_3x3
print("\nРезультат сложения:\n", result_array)
print('\nЗадание 2')


array_6x6 = np.random.rand(6, 6)
print("Исходный массив 6x6:\n", array_6x6)

second_row = array_6x6[1]
print("\n2-я строка:\n", second_row)

last_two_cols = array_6x6[:, -2:]
print("\nПоследние два столбца:\n", last_two_cols)

np.fill_diagonal(array_6x6, 0)
print("\nМассив с нулевой главной диагональю:\n", array_6x6)

array_1_15 = np.arange(1, 16)
print("Исходный массив:", array_1_15)

first_five = array_1_15[:5]
print("Первые 5 элементов:", first_five)

every_second = array_1_15[::2]
print("Каждый второй элемент:", every_second)

last_five_reversed = array_1_15[-1:-6:-1]
print("Последние 5 элементов в обратном порядке:", last_five_reversed)

print('\nЗадание 3')
# Загрузка датасета (этот код уже был в документе)
import gdown, pandas as pd
file_id = "1qq6rk9YwRE_AwxUO7_xbRwq0OJPwtYsb"
url = f"https://drive.google.com/uc?id={file_id}"
gdown.download(url, "robot_dataset.csv", quiet=True)
df = pd.read_csv("robot_dataset.csv")

unique_temperatures = df['temperature'].unique()
print("Уникальные значения температуры (первые 20):", unique_temperatures[:20])

temperature_counts = df['temperature'].value_counts()
print("\nЧастота встречаемости значений температуры (топ-10):\n", temperature_counts.head(10))