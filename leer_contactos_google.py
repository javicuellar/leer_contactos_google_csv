import pandas as pd


df = pd.read_csv('contacts.csv', delimiter=',')

df5 = df.tail(5)

print(df5.columns)

# Iteración por filas del DataFrame:
print("Iterando filas")
for i in range(len(df5)):
	fila = df5.iloc[i]
	# Reemplazar NaN con un valor temporal (por ejemplo, -999)
	valor_temporal = -999
	fila_con_relleno = fila.fillna(valor_temporal)
	# Recorrer la fila sin leer NaN
    valo6res = [valor for valor in fila_con_relleno if valor != valor_temporal]
    
    for col in df5.columns:
		if df5.iloc[i][col].isna():
			dato = df5.iloc[i][col]
			fila += f"{col}: {dato} - " 
	print(fila)
	exit()
	
    # Obtener la fila deseada (por ejemplo, la primera fila)
fila = df.iloc[0]

# Reemplazar NaN con un valor temporal (por ejemplo, -999)
valor_temporal = -999
fila_con_relleno = fila.fillna(valor_temporal)

# Recorrer la fila sin leer NaN
valores = [valor for valor in fila_con_relleno if valor != valor_temporal]

    # if dato == '':
	# 	print("nulo")
#	col = df5.columns[0]
#	print(f"{col} -> {df5.iloc[i][col]}")