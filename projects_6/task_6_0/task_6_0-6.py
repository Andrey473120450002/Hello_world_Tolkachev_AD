import pandas as pd

df = pd.read_csv('wild_boars.csv')
males = df[df['gender'] == 'Male']['length_cm']
females = df[df['gender'] == 'Female']['length_cm']

q1_m = males.quantile(0.25)
q3_m = males.quantile(0.75)
iqr_m = q3_m - q1_m

q1_f = females.quantile(0.25)
q3_f = females.quantile(0.75)
iqr_f = q3_f - q1_f

with open('task_6_0-6_iqr.txt', 'w', encoding='utf-8') as f:
    f.write(f"Male: IQR = {iqr_m:.1f} cm (Q1={q1_m:.1f}, Q3={q3_m:.1f})\n")
    f.write(f"Female: IQR = {iqr_f:.1f} cm (Q1={q1_f:.1f}, Q3={q3_f:.1f})\n")
print("IQR по длине тела сохранён в task_6_0-6_iqr.txt")
