import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("netflix_titles.csv")

df["fecha_convertida"] = pd.to_datetime(df["date_added"].str.strip(), errors="coerce")

df_clean = df.dropna(subset=["fecha_convertida"])

plt.figure(figsize=(10, 6))
plt.hist(df_clean["fecha_convertida"], bins=20, edgecolor="black", color="skyblue")

plt.title("Histograma de adición de títulos a Netflix")
plt.xlabel("Año de adición")
plt.ylabel("Cantidad de títulos")
plt.gcf().autofmt_xdate()

plt.savefig("graphics/matplotlib.png")
