import requests
user_genre= "Romance"
api_key = '9ae4aa8fd098519b71e941c397067bc3'
movie_id = 27  

# Make the request
url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse the JSON response
    movie_data = response.json()
    # Extract relevant information
    id=movie_data['id']
    title = movie_data['title']
    overview = movie_data['overview']
    release_date = movie_data['release_date']
    genres=movie_data['genres']

    print(f'Title: {title}\nOverview: {overview}\nRelease Date: {release_date}\nGenre: {genres}')

    for genre in genres:
        genre_name = genre['name']
        print("Genre Name:", genre_name)

    if genre_name[2]  != user_genre:
        print('esit degil')
        movie_id+=1
    else:
        print("esiT")
        print(f'Title: {title}\nOverview: {overview}\nRelease Date: {release_date}\nGenre: {genre}')
else:
    print('Failed to fetch movie details.')

