import requests


app_authorization = "Basic ODA3M2VlMGYxNmE2NDc3NGJkMGU3ZjhmYTk1NWI5ZDY6MmEyNGVmM2U2NjkwNGVlYWI4MjRhODc3Mjg5MDU1M2Q="


# Retrieves access token from spotify API
# parameter auth_code(str): authentication code returned by spotify after user logins
# return access_token(str): access token needed to retrieve user data
def get_access_token(auth_code):
    spotify_auth_url = "https://accounts.spotify.com/api/token"
    body = {
        'grant_type': "authorization_code",
        'code': auth_code,
        'redirect_uri': "http://localhost:3000/callback"
    }
    headers = {
        "Authorization": app_authorization
    }

    return requests.post(spotify_auth_url, data=body, headers=headers).json()['access_token']


def get_top_songs(access_token):
    top_songs_url = "https://api.spotify.com/v1/me/top/tracks"

    headers = {
        "Authorization": "Bearer " + access_token
    }

    user_data = requests.get(top_songs_url, headers=headers).json()

    songs = []

    for item in user_data['items']:
        artists = []
        for artist in item['album']['artists']:
            artists.append({
                'artist_name': artist['name']
            })
        songs.append({
            'artists': artists,
            'name': item['album']['name'],
            'id': item['album']['id']
        })

    return songs





