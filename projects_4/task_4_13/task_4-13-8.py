a = [-15, 42, -7, 0, -23, 99, -3]
n = len(a)
i = 0
sum = 0
while i < n:
    if a[i] > 0:
        sum = sum + 1
    i = i + 1
print(f"Количествo положительных чисел массиве равно {sum}")