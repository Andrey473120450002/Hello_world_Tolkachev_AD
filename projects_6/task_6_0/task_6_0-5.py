import pandas as pd

df = pd.read_csv('wild_boars.csv')
numeric_cols = df.select_dtypes(include='number').columns
percentiles = [0.25, 0.50, 0.75, 0.90, 0.95, 1.00]
labels = [
    "Percentile 25 (Q1)",
    "Median 50 (Q2)",
    "Percentile 75 (Q3)",
    "Percentile 90",
    "Percentile 95",
    "Max"
]

with open('task_6_0-5_percentiles.txt', 'w', encoding='utf-8') as f:
    for col in numeric_cols:
        f.write(f"{col}:\n")
        for p, label in zip(percentiles, labels):
            value = df[col].quantile(p)
            unit = ""
            if "weight" in col.lower():
                unit = "kg"
            elif "length" in col.lower() or "tusk" in col.lower():
                unit = "cm"
            f.write(f"{label}:\t{value:.1f} {unit}\n".expandtabs(4))
        f.write("\n")
print("Перцентили сохранены в task_6_0-5_percentiles.txt")
