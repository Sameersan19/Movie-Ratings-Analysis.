
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("movie_ratings_2024.csv")  # Replace with actual dataset
df.head()
df = pd.read_csv(r"C:\Users\Ahmes\Onedrive\Desktop\movie_ratings_2024.csv")
print(df.info())  # Check column types and missing values
print(df.describe())  # Get statistical summary
top_movies = df[['Title', 'Rating']].sort_values(by='Rating', ascending=False).head(10)
print(top_movies)
most_reviewed = df[['Title', 'Votes']].sort_values(by='Votes', ascending=False).head(10)
print(most_reviewed)
avg_rating_per_genre = df.groupby('Genre')['Rating'].mean().sort_values(ascending=False)
print(avg_rating_per_genre)
plt.figure(figsize=(10,5))
plt.hist(df['Rating'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Rating')
plt.ylabel('Number of Movies')
plt.title('Distribution of Movie Ratings')
plt.show()
