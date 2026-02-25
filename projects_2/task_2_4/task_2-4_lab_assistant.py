volume = float(input("Введите нужный объем раствора (в мл): "))
salt_mass = volume * 0.009
water_volume = volume
with open("recipe.txt", "w", encoding="utf-8") as file:
file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
file.write("===" * 4)
file.write(f"Общий объем: {volume} \nмл Масса соли: {salt_mass:.2f} г \nОбъем воды: {water_volume}мл")