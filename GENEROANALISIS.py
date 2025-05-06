import pandas as pd
import matplotlib.pyplot as plt


peliculas_df = pd.read_csv("Data/Rotten Tomatoes Movies.csv")


peliculas_df['fecha_estreno'] = pd.to_datetime(peliculas_df['in_theaters_date'], errors='coerce')


peliculas_copia = peliculas_df.copy()


generos_explotados = peliculas_copia.assign(
    genero=peliculas_copia['genre'].dropna().str.split(',')
).explode('genero')


generos_explotados['genero'] = generos_explotados['genero'].str.strip()


promedio_por_genero = generos_explotados.groupby('genero')['audience_rating'].mean().sort_values(ascending=False)


print("Top 10 géneros con mayor promedio de audiencia:\n")
print(promedio_por_genero.head(10))


top_10_generos = promedio_por_genero.head(10)


plt.figure(figsize=(7,7))
top_10_generos.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Top 10 géneros por calificación promedio de audiencia")
plt.ylabel("")
plt.tight_layout()
plt.show()
