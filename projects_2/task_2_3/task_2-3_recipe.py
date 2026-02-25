nutrient_medium = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temperature = input("Введите температуру стерилизации (°C): ")
with open("recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"\t{nutrient_medium}")
    recipe.write(f"\nКонцентрация агара (%): {agar_concentration}")
    recipe.write(f"\nТемпература стерилизации (°C): {sterilization_temperature}")
print("Файл 'recipe.txt' успешно сформирован!")