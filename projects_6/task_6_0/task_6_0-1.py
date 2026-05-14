import pandas as pd

df = pd.read_csv('wild_boars.csv')
print("Столбец 'tusk_length_cm':")
print(df['tusk_length_cm'])

min_tusk = df['tusk_length_cm'].min()
max_tusk = df['tusk_length_cm'].max()
print(f"\nСамый короткий клыки: {min_tusk} см")
print(f"Самый длинный клыки: {max_tusk} см")
