import pandas as pd

df = pd.read_csv('wild_boars.csv')
numeric_cols = df.select_dtypes(include='number').columns
means = df[numeric_cols].mean()

with open('task_6_0-2_means.txt', 'w', encoding='utf-8') as f:
    for col, val in means.items():
        f.write(f"{col}: {val:.2f}\n")
print("Средние сохранены в task_6_0-2_means.txt")
