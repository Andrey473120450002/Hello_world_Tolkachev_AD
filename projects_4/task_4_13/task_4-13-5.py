n = int(input("Введите целое число: "))
a = float(input("Введите первое число: "))
i = 2
max = a
while i <= n:
    a = float(input("Введите следующее число: "))
    if a > max:
        max = a
    i = i + 1
print(f"Максимальное из {n} введенных чисел равно {max}")