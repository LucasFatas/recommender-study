import requests
from src.Entities.Song import Song


class AuthorizationException(Exception):
    pass


class InvalidAccountException(Exception):
    pass


app_authorization = "Basic ODA3M2VlMGYxNmE2NDc3NGJkMGU3ZjhmYTk1NWI5ZDY6MmEyNGVmM2U2NjkwNGVlYWI4MjRhODc3Mjg5MDU1M2Q="


def get_access_token(auth_code):
    """
    Retrieves the token of a participant after logging in the app
    :param auth_code: login credentials of the user
    :raise AuthorizationException: if there is an error retrieving the token
    :return: the access token for the app
    """
    spotify_auth_url = "https://accounts.spotify.com/api/token"
    body = {
        'grant_type': "authorization_code",
        'code': auth_code,
        'redirect_uri': "http://localhost:3000/spotify/callback"
    }
    headers = {
        "Authorization": app_authorization
    }
    r = requests.post(spotify_auth_url, data=body, headers=headers)

    if r.status_code == 400:
        raise AuthorizationException("Error requesting access token")

    return r.json()['access_token']


def get_top_songs_api(access_token):
    """
    Retrieve the 5 top songs (with non-null URL preview link) of a given user after logging in
    :param access_token: the access token of the logged in participant
    :raise AuthorizationException: if there is an error with the token verification
    :raise InvalidAccountException: if the participant has less than 5 songs, refuse his participation
    :return: a list of 5 top songs of the participant.
    """
    top_songs_url = "https://api.spotify.com/v1/me/top/tracks?limit=5"

    headers = {
        "Authorization": "Bearer " + access_token
    }
    r = requests.get(top_songs_url, headers=headers)

    if r.status_code == 401:
        raise AuthorizationException("Error Retrieving Top Songs. Access_token could be outdated or wrong")

    user_data = r.json()

    # Check if the user has less than 5 songs.
    if len(user_data['items']) < 5:
        raise InvalidAccountException("Not enough top tracks")

    # Create the list of songs from the user.
    songs = []
    index = 0
    # Keep retrieving the next song if the current one's link is null, and we still haven't reached 5 songs.
    while len(songs) < 5:
        item = user_data['items'][index]
        artists = []
        for artist in item['artists']:
            artists.append({
                'artist_name': artist['name']
            })
        # Check that the preview_url of the song is not empty.
        if item['preview_url'] != "" or item['preview_url'] is not None:
            songs.append(Song(item['preview_url'], item['name'], artists, item['external_urls']['spotify']))
        index += 1

    return songs
