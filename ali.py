#19 вариант
# Задача 1
A = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

num_rows = 4
num_cols = 5

for col in range(num_cols):
    column_sum = 0
    for row in range(num_rows):
        column_sum += A[row][col]
    average = column_sum / num_rows
    print(f"Среднее арифметическое столбца {col}: {average}")

# Задача 2
B = list(range(30))  # пример массива из чисел 0..29

sum_odd_indices = 0
for i in range(1, 30, 2):
    sum_odd_indices += B[i]

print(f"Сумма элементов с нечетными индексами: {sum_odd_indices}")
