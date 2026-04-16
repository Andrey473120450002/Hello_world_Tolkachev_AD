a = [8, 22, 37, 5, 64, 19, 73]
n = len(a)
i = 0
sum = 0
cou = 0
while i < n:
    sum = sum + a[i]
    cou = cou + 1
    i = i + 2
if cou > 0:
    medium = round(sum / cou, 2)
else:
    medium = 0
print(f"Среднее арифметическое элементов с четными индексами в массиве равно {medium}")