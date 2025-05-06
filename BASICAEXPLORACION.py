import pandas as pd
import matplotlib.pyplot as plt


peliculas_df = pd.read_csv("Data/Rotten Tomatoes Movies.csv")


peliculas_df['fecha_estreno'] = pd.to_datetime(peliculas_df['in_theaters_date'], errors='coerce')


total_peliculas = len(peliculas_df)
print(f"Total de películas en el dataset: {total_peliculas}")


distribucion_tomatometro = peliculas_df['tomatometer_status'].value_counts()
print("\nDistribución de calificaciones del tomatómetro:")
print(distribucion_tomatometro)


plt.figure(figsize=(6,6))
distribucion_tomatometro.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Distribución de calificaciones (Tomatómetro)")
plt.ylabel("")
plt.tight_layout()
plt.show()
