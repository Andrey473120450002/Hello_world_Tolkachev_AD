import pandas as pd

df = pd.read_csv('wild_boars.csv')
numeric_cols = df.select_dtypes(include='number').columns

with open('task_6_0-7_variation.txt', 'w', encoding='utf-8') as f:
    for col in numeric_cols:
        var = df[col].var()
        std = df[col].std()
        mean_val = df[col].mean()
        cv = (std / mean_val * 100) if mean_val != 0 else 0
        f.write(f"{col}:\n")
        f.write(f"  Дисперсия: {var:.2f}\n")
        f.write(f"  Стандартное отклонение: {std:.2f}\n")
        f.write(f"  Коэффициент вариации: {cv:.2f}%\n\n")
print("Показатели вариации сохранены в task_6_0-7_variation.txt")
