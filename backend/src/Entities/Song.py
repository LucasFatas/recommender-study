class Song:

    def __init__(self, preview_url, name, artists, spotify_url):
        """
        Entity that stores all relevant information about the songs fetched from Spotify
        :param preview_url: URL that sends you to a MP3 30-second snippet of the song
        :param name: name of the song
        :param artists: list with artists of the song
        :param spotify_url: Official Spotify URL that identifies the song within this service
        """
        self.artists = artists
        self.name = name
        self.spotify_url = spotify_url
        self.preview_url = preview_url


