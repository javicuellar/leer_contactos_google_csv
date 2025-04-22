import pandas as pd


df = pd.read_csv('contacts.csv', delimiter=',')

df5 = df.tail(5)

print(df5.columns)

# Iteración por filas del DataFrame:
print("Iterando filas")
for i in range(len(df5)):
	col = df5.columns[0]
	print(f"{col} -> {df5.iloc[i][col]}")