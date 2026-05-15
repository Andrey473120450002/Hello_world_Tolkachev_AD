import pandas as pd

df = pd.read_csv('wild_boars.csv')
males = df[df['gender'] == 'male']['tusk_length_cm']
females = df[df['gender'] == 'female']['tusk_length_cm']

def cv(series):
    return (series.std() / series.mean() * 100) if series.mean() != 0 else 0

cv_male = cv(males)
cv_female = cv(females)

with open('task_6_0-8_cv_tusks.txt', 'w', encoding='utf-8') as


f:
    f.write(f"Male tusk length CV: {cv_male:.2f}%\n")
    f.write(f"Female tusk length CV: {cv_female:.2f}%\n")
print("Коэффициенты вариации клыков сохранены в task_6_0-8_cv_tusks.txt")
