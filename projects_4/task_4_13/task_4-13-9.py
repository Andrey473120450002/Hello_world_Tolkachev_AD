a = [3, 15, 27, 41, 56, 9, 63]
n = len(a)
i = 0
sum = 0
while i < n:
    if a[i] % 2 != 0:
        sum = sum + a[i]
    i = i + 1
print(f"Сумма всех нечетных элементов в массиве равна {sum}")