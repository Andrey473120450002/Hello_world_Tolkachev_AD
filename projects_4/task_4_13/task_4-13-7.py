a = [23, 67, 21, 12, 89, 45, 76]
n = len(a)
i = 0
sum = 0
while i < n:
    sum = sum + a[i]
    i = i + 1
medium = round(sum / n, 2)
print(f"Среднее арифметическое элементов массива равно {medium}")