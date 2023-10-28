import requests

def search_spotify(query):
    # Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' with your Spotify app's credentials
    client_id = '92f6f39fbb1348b8ab89f1b1f56e308a'
    client_secret = '0bc1273cf7fe422491b96e64f4dbdbe7'

    # Authenticate with the Spotify API
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }
    auth_response = requests.post(auth_url, data=auth_data)
    auth_token = auth_response.json()['access_token']

    # Use the access token to search for songs
    headers = {
        'Authorization': f'Bearer {auth_token}',
    }
    search_url = f'https://api.spotify.com/v1/search?q={query}&type=track'
    response = requests.get(search_url, headers=headers)
    data = response.json()

    with open("Spotify//response.txt","w") as writer:
      writer.write(str(data))

    # Display the search results
    for track in data['tracks']['items']:
        print(f"Title: {track['name']}")
        print(f"Artist: {track['artists'][0]['name']}")
        print(f"Album: {track['album']['name']}")
        print(f"Album_type: {track['album']['album_type']}")
        print(f"Url: {track['external_urls']['spotify']}")
        print('---')

# Example usage
search_query = 'Travis Scott'
search_spotify(search_query)
