import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Загрузка данных ---
print("Загрузка данных...")
url = "https://drive.google.com/uc?export=download&id=1MVbh3ReFZEw3uKreAj2s0ftYiUHvT0qa"
df = pd.read_csv(url)
print("Данные загружены. Первые 5 строк:")
print(df.head())
print("-" * 50)

# --- Задание 1: Преобразование Unix-времени ---
print("Задание 1: Преобразование столбца 'ts' в формат даты и времени...")
df['ts'] = pd.to_datetime(df['ts'], unit='s')
print("Столбец 'ts' преобразован. Первые 5 строк с новым форматом:")
print(df.head())
print("-" * 50)

# --- Задание 2: Группировка по устройству ---
print("Задание 2: Группировка данных по устройству...")
agg_funcs = {
    'temp': 'mean',
    'humidity': 'max',
    'co': 'min',
    'device': 'count'
}
device_stats = df.groupby('device').agg(agg_funcs).rename(columns={'device': 'count'})
print("Статистика по устройствам:")
print(device_stats)
print("-" * 50)

# --- Задание 3: Группировка по движению ---
print("Задание 3: Группировка данных по движению...")
motion_stats = df.groupby('motion')[['temp', 'humidity', 'lpg']].mean()
print("Статистика по движению:")
print(motion_stats)
print("-" * 50)

# --- Задание 4: Сводная таблица ---
print("Задание 4: Создание сводной таблицы...")
pivot_table = pd.pivot_table(df, values='temp', index='device', columns='motion', aggfunc='mean')
print("Сводная таблица средней температуры по движению:")
print(pivot_table)
print("-" * 50)

# --- Задание 5: Создание нового столбца 'temp_category' ---
print("Задание 5: Создание столбца 'temp_category'...")
def categorize_temp(temp):
    if temp < 20:
        return 'Холодно'
    elif 20 <= temp <= 25:
        return 'Нормально'
    else:
        return 'Жарко'

df['temp_category'] = df['temp'].apply(categorize_temp)
print("Столбец 'temp_category' добавлен. Первые 5 строк с новым столбцом:")
print(df.head())
print("-" * 50)

# --- Задание 6: Группировка по категории температуры ---
print("Задание 6: Группировка по 'temp_category'...")
temp_category_stats = df.groupby('temp_category').agg(
    smoke_mean=('smoke', 'mean'),
    co_mean=('co', 'mean'),
    count=('temp_category', 'count')
)
print("Статистика по категориям температуры:")
print(temp_category_stats)
print("-" * 50)

# --- Задание 7: Построение столбчатой диаграммы ---
print("Задание 7: Построение столбчатой диаграммы средней температуры по устройствам...")
avg_temp_by_device = df.groupby('device')['temp'].mean()
plt.figure(figsize=(10, 6))
avg_temp_by_device.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Средняя температура по устройствам')
plt.xlabel('Устройство')
plt.ylabel('Средняя температура (°C)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.show()
print("График построен.")