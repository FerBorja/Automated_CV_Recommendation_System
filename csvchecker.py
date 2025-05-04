import pandas as pd
df = pd.read_csv("data/Resume.csv")
print("Columnas disponibles:", df.columns.tolist())
print("Primeras filas:\n", df.head())