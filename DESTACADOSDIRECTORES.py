import pandas as pd
import matplotlib.pyplot as plt


peliculas_df = pd.read_csv("Data/Rotten Tomatoes Movies.csv")


peliculas_df['fecha_estreno'] = pd.to_datetime(peliculas_df['in_theaters_date'], errors='coerce')


conteo_por_director = peliculas_df['directors'].value_counts()


top_10_directores = conteo_por_director.head(10)
print("Top 10 directores con más películas:\n")
print(top_10_directores)


nombres_top_10 = top_10_directores.index.tolist()
peliculas_top_directores = peliculas_df[peliculas_df['directors'].isin(nombres_top_10)].copy()


promedio_tomatometro = peliculas_top_directores.groupby('directors')['tomatometer_rating'].mean().sort_values(ascending=False)

print("\nPromedio de calificación del tomatómetro por cada uno de los 10 directores:")
print(promedio_tomatometro)


top_5_directores = promedio_tomatometro.head(5)


plt.figure(figsize=(8,5))
top_5_directores.plot(kind='bar', color='salmon', edgecolor='black')
plt.title("Top 5 directores con mejor calificación promedio del tomatómetro")
plt.xlabel("Director")
plt.ylabel("Promedio tomatometer_rating")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y')
plt.show()
