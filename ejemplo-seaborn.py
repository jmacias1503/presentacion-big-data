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

plt.title("Distribucion de titulos por ano - Netflix", fontsize=14)
plt.xlabel("Ano")
plt.ylabel("Cantidad de titulos")

plt.savefig("seaborn.png", dpi=150, bbox_inches="tight")
