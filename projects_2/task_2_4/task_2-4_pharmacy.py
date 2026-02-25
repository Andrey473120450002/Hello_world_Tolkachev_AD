total = int(input("Введите общее количество произведенных капсул: "))
pack_capacity = int(input("Введите количество капсул в одной упаковке: "))
full_packs = total // pack_capacity
remnant = total % pack_capacity
print("--- Отчет фасованного цеха ---")
print(f"Полных упаковок: {full_packs}")
print(f"Остаток капсул: {remnant}")