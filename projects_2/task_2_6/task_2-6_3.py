donor = input("Введите группу крови донора (I,II,III,IV)").strip().upper()
recipient = input("Введите группу крови пациент (I,II,III,IV)").strip().upper()
if donor == recipient or donor == "I":
    print("Переливание возможно")
else:
    print("Переливание невозможно")    