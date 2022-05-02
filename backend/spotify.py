import requests


app_authorization = "Basic ODA3M2VlMGYxNmE2NDc3NGJkMGU3ZjhmYTk1NWI5ZDY6MmEyNGVmM2U2NjkwNGVlYWI4MjRhODc3Mjg5MDU1M2Q="


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

    print(access_token)
    headers = {
        "Authorization": "Bearer " + access_token
    }

    return requests.get(top_songs_url, headers=headers)




