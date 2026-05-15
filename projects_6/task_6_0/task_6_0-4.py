import pandas as pd

df = pd.read_csv('wild_boars.csv')

with open('task_6_0-4_modes.txt', 'w', encoding='utf-8') as f:
    for col in df.columns:
        if 'id' in col.lower():
            f.write(f"{col}: Мода не применима \n")
            continue

        mode_series = df[col].mode()
        if mode_series.empty:
            mode_str = "Нет моды"
        else:
            # здесь отступ должен быть одинаковым (4 пробела)
            if len(mode_series) == len(df[col].dropna()):
                mode_str = "Все значения уникальные, мода не определима"
            else:
                mode_str = ", ".join(map(str, mode_series.values))
        f.write(f"{col}: {mode_str}\n")

print("Моды сохранены в task_6_0-4_modes.txt")
