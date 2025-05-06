import pandas as pd
import matplotlib.pyplot as plt


peliculas_df = pd.read_csv("Data/Rotten Tomatoes Movies.csv")


print("Primeras 5 filas del DataFrame:\n")
print(peliculas_df.head())


print("\nTipos de datos antes de la conversión:\n")
print(peliculas_df.dtypes)


peliculas_df['fecha_estreno'] = pd.to_datetime(peliculas_df['in_theaters_date'], errors='coerce')


print("\nTipos de datos después de la conversión:\n")
print(peliculas_df.dtypes)


fechas_faltantes = peliculas_df['fecha_estreno'].isna().sum()
print(f"\nPelículas con fechas no reconocidas: {fechas_faltantes}")
