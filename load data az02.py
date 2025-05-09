import pandas as pd
import numpy as np

# 1. Создаем DataFrame с данными об оценках 10 учеников
data = {
    'Ученик': ['Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Смирнов',
              'Васильев', 'Павлов', 'Семенов', 'Голубев', 'Козлов'],
    'Математика': [5, 4, 3, 5, 4, 3, 5, 4, 3, 2],
    'Физика': [4, 5, 4, 3, 4, 5, 4, 3, 2, 4],
    'Химия': [3, 4, 5, 4, 3, 2, 4, 5, 4, 3],
    'Литература': [4, 3, 4, 5, 4, 3, 2, 4, 5, 4],
    'История': [5, 4, 3, 2, 5, 4, 3, 4, 5, 4]
}

df = pd.DataFrame(data)

# 2. Выводим первые строки для проверки
print("Первые 5 строк данных:")
print(df.head())

# 3. Вычисляем среднюю оценку по каждому предмету
print("\nСредние оценки по предметам:")
print(df.mean(numeric_only=True))

# 4. Вычисляем медианную оценку по каждому предмету
print("\nМедианные оценки по предметам:")
print(df.median(numeric_only=True))

# 5. Вычисляем квартили для математики
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print(f"\nДля математики: Q1 = {Q1_math}, Q3 = {Q3_math}, IQR = {IQR_math}")

# 6. Вычисляем стандартное отклонение
print("\nСтандартное отклонение по предметам:")
print(df.std(numeric_only=True))
