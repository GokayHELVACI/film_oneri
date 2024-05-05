import requests
user_genre= "Drama"
user_input= user_genre #Change this into an actual input
api_key = '**'
movie_id = 260  

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

    
    found = False
    for genre in genres:
        if user_input.lower() == genre['name'].lower():
            found = True
            break
    if found:
        print("Başarılı")
    else:
        print("Genre not found")
else:
    print('Failed to fetch movie details.')
