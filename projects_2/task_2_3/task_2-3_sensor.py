operator_name = input("Введите имя оператора: ")
pressure = input("Введите текущее значение давления (Па): ")
with open("sensor_log.txt", "w", encoding="utf-8") as log:
    log.write(f"ОПЕРАТОР\tЗНАЧЕНИЕ\n{operator_name}\t{pressure}")
print("Данные успешно сохранены в sensor_log.txt ")