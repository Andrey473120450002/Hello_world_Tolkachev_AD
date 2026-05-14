import pandas as pd

df = pd.read_csv('wild_boars.csv')
numeric_cols = df.select_dtypes(include='number').columns
medians = df[numeric_cols].median()

with open('task_6_0-3_medians.txt', 'w', encoding='utf-8') as f:
    for col, val in medians.items():
        f.write(f"{col}: {val:.2f}\n")
print("Медианы сохранены в task_6_0-3_medians.txt")
