n = int(input("Введите целое число: "))
i = 1
factorial = 1
while i <= n:
    factorial = factorial * i
    i = i + 1
print(f"Факториал {n} равен {factorial}")