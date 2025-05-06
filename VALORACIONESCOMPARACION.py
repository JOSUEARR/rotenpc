import pandas as pd
import matplotlib.pyplot as plt


peliculas_df = pd.read_csv("Data/Rotten Tomatoes Movies.csv")


peliculas_df['fecha_estreno'] = pd.to_datetime(peliculas_df['in_theaters_date'], errors='coerce')


promedio_criticos = peliculas_df['tomatometer_rating'].mean()
promedio_audiencia = peliculas_df['audience_rating'].mean()


print(f"Promedio de valoración por críticos: {promedio_criticos:.2f}")
print(f"Promedio de valoración por audiencia: {promedio_audiencia:.2f}")


peliculas_df['diferencia_valoracion'] = peliculas_df['audience_rating'] - peliculas_df['tomatometer_rating']


plt.figure(figsize=(8,5))
plt.hist(peliculas_df['diferencia_valoracion'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title("Diferencia entre valoraciones (Audiencia - Críticos)")
plt.xlabel("Diferencia de puntuación")
plt.ylabel("Cantidad de películas")
plt.grid(True)
plt.tight_layout()
plt.show()
