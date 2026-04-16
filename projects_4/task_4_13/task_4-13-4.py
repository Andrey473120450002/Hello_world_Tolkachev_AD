n = int(input("Введите целое число: "))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 1
print (f"Сумма первых {n} натуральных чисел равна {sum}")