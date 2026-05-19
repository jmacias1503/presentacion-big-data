import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("netflix_titles.csv")

df_clean = df.dropna(subset=["date_added"])
df_clean["date_added"] = pd.to_datetime(
    df_clean["date_added"].str.strip(), errors="coerce"
)
df_clean = df_clean.dropna(subset=["date_added"])

df_clean["year"] = df_clean["date_added"].dt.year
df_clean["month"] = df_clean["date_added"].dt.month

plt.figure(figsize=(12, 6))
sns.histplot(data=df_clean, x="year", bins=15, kde=True, color="purple")

plt.title("Distribución de títulos por año - Netflix", fontsize=14)
plt.xlabel("Año")
plt.ylabel("Cantidad de títulos")

plt.savefig("graphics/seaborn.png", dpi=150, bbox_inches="tight")
