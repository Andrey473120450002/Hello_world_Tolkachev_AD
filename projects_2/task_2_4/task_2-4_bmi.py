weight = float(input("Введите ваш вес (кг): "))
height_cm = float(input("Введите ваш рост (см): "))
height_m = height_cm / 100
bmi = weight / (height_m ** 2)
print("--- Отчет о состоянии здоровья ---")
print(f"Рост: {height_cm} см")
print(f"Вес: {weight} кг")
print(f"Индекс массы тела: {bmi}")