import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Загрузка данных
df = pd.read_csv('amazon_sales_data 2025.csv')

# 2. Оценка пропусков и структуры
def dataset_overview(data):
    print('Колонки:', data.columns.tolist())
    print('Размер:', data.shape)
    print('Пропуски:')
    print(data.isnull().sum())
    print('\nПервые строки:')
    print(data.head())
    print('\nСтатистика:')
    print(data.describe(include="all"))

dataset_overview(df)

# 3. Анализ категориальных и числовых признаков
print('\nЧастоты по Category:')
print(df['Category'].value_counts())
print('\nЧастоты по Payment Method:')
print(df['Payment Method'].value_counts())
print('\nЧастоты по Status:')
print(df['Status'].value_counts())
print('\nЧастоты по Product:')
print(df['Product'].value_counts())

# 4. Топ-5 покупателей по Total Sales
top_buyers = df.groupby('Customer Name')['Total Sales'].sum().sort_values(ascending=False).head(5)
print('\nТоп-5 покупателей по суммарным покупкам:')
print(top_buyers)

# 5. Топ-5 товаров по доходу
top_products = df.groupby('Product')['Total Sales'].sum().sort_values(ascending=False).head(5)
print('\nТоп-5 товаров по сумме продаж:')
print(top_products)

# 6. Визуализация
plt.figure(figsize=(8,5))
sns.barplot(x=df['Category'].value_counts().index, y=df['Category'].value_counts().values)
plt.title('Число заказов по категориям товаров')
plt.ylabel('Число заказов')
plt.xlabel('Категория')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,6))
df['Status'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Распределение статусов заказов')
plt.ylabel('')
plt.show()
