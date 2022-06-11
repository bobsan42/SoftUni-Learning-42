n_movies = int(input())
top_film = ''
top_rating = 0
last_film = ''
last_rating = 10
sum_ratings = 0

for m in range(n_movies):
    title = input()
    rating = float(input())
    sum_ratings += rating
    if rating < last_rating:
        last_rating = rating
        last_film = title
    if rating > top_rating:
        top_rating = rating
        top_film = title
avg_rating = sum_ratings / n_movies

print(f"{top_film} is with highest rating: {top_rating:.1f}")
print(f"{last_film} is with lowest rating: {last_rating:.1f}")
print(f"Average rating: {avg_rating:.1f}")
