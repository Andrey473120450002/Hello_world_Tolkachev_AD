a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
d = float(input("Введите четвертое число: "))
if a < b and a < c and a < d:
    min = a
elif b > d and c > d and a > d:
    min = d
elif a > c and b > c and d > c:
    min = c
elif a > b and c > b and d > b:
    min = b
print("Минимальное число: ", min)