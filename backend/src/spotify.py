import requests
from src.Entities.Song import Song


class AuthorizationException(Exception):
    pass


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
    r = requests.post(spotify_auth_url, data=body, headers=headers)

    if r.status_code == 400:
        raise AuthorizationException("Error requesting access token")

    return r.json()['access_token']


def get_top_songs_api(access_token):
    top_songs_url = "https://api.spotify.com/v1/me/top/tracks"

    headers = {
        "Authorization": "Bearer " + access_token
    }
    r = requests.get(top_songs_url, headers=headers)

    if r.status_code == 401:
        AuthorizationException("Error Retrieving Top Songs. Access_token could be outdated or wrong")

    user_data = r.json()

    songs = []

    for item in user_data['items']:
        artists = []
        for artist in item['album']['artists']:
            artists.append({
                'artist_name': artist['name']
            })

        songs.append(Song(item['album']['id'], item['album']['name'], artists))

    return songs
