import requests, os
from dotenv import load_dotenv

from src.Entities.Song import Song


class AuthorizationException(Exception):
    pass


class InvalidAccountException(Exception):
    pass


load_dotenv()

app_authorization = "Basic ODA3M2VlMGYxNmE2NDc3NGJkMGU3ZjhmYTk1NWI5ZDY6MmEyNGVmM2U2NjkwNGVlYWI4MjRhODc3Mjg5MDU1M2Q="
port = os.getenv('PORT')


# Retrieves access token from spotify API
# parameter auth_code(str): authentication code returned by spotify after user logins
# return access_token(str): access token needed to retrieve user data
def get_access_token(auth_code):
    spotify_auth_url = "https://accounts.spotify.com/api/token"
    body = {
        'grant_type': "authorization_code",
        'code': auth_code,
        'redirect_uri': f"http://localhost:{port}/spotify/callback"
    }
    headers = {
        "Authorization": app_authorization
    }
    r = requests.post(spotify_auth_url, data=body, headers=headers)

    if r.status_code == 400:
        raise AuthorizationException("Error requesting access token")

    return r.json()['access_token']


def get_top_songs_api(access_token):
    top_songs_url = "https://api.spotify.com/v1/me/top/tracks?limit=5"

    headers = {
        "Authorization": "Bearer " + access_token
    }
    r = requests.get(top_songs_url, headers=headers)

    if r.status_code == 401:
        raise AuthorizationException("Error Retrieving Top Songs. Access_token could be outdated or wrong")

    user_data = r.json()

    if len(user_data['items']) < 5:
        raise InvalidAccountException("Not enough top tracks")
    songs = []
    index = 0
    while len(songs) < 5:
        item = user_data['items'][index]
        artists = []
        for artist in item['artists']:
            artists.append({
                'artist_name': artist['name']
            })
        if item['preview_url'] != "" or item['preview_url'] is not None:
            songs.append(Song(item['preview_url'], item['name'], artists, item['external_urls']['spotify']))
        index += 1

    return songs
