n = int(input("Введите целое число: "))
i = 1
sum = 0
while i <= n:
    sum = sum + i * i
    i = i + 1
print(f"Сумма квадратов первых {n} чисел равна {sum}")