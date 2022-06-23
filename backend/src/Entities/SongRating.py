class SongRating:

    def __init__(self, userId, matchedUserId, spotify_url, rating, playlist_number):
        """
        Entity that stores the ratings provided by a user for specific songs
        :param userId: id of the participant
        :param matchedUserId: id of the participant he matched with
        :param spotify_url: URL of the Spotify song he is rating
        :param rating: rating provided, can be zero
        :param playlist_number: index of the song within the matched user's top songs (1 to 5)
        """
        self.userId = userId
        self.matchedUserId = matchedUserId
        self.spotify_url = spotify_url
        self.rating = rating
        self.playlistNumber = playlist_number
