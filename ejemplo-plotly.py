import pandas as pd
import plotly.express as px

df = pd.read_csv("netflix_titles.csv")

movies_df = df[df["type"] == "Movie"].copy()

movies_df["country"] = movies_df["country"].fillna("Unknown")
movies_df["country"] = movies_df["country"].str.split(", ")
movies_exploded = movies_df.explode("country")

top_5_countries = movies_exploded["country"].value_counts().head(5).index.tolist()

filtered_df = movies_exploded[movies_exploded["country"].isin(top_5_countries)]

rating_counts = (
    filtered_df.groupby(["country", "rating"]).size().reset_index(name="movie_count")
)

top_3_ratings = (
    rating_counts.sort_values(["country", "movie_count"], ascending=[True, False])
    .groupby("country")
    .head(3)
)

top_3_ratings["country"] = pd.Categorical(
    top_3_ratings["country"], categories=top_5_countries, ordered=True
)
top_3_ratings = top_3_ratings.sort_values("country")

fig = px.bar(
    top_3_ratings,
    x="country",
    y="movie_count",
    color="rating",
    barmode="group",
    title="Las 3 clasificaciones de peliculas populares en los top 5 paises con mas producciones",
    labels={
        "country": "Pais",
        "movie_count": "Peliculas",
        "rating": "Clasificacion",
    },
    text_auto=True,
    template="plotly_white",
)

fig.update_layout(xaxis={"categoryorder": "array", "categoryarray": top_5_countries})

fig.write_image("plotly.png")
