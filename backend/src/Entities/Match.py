class Match:

    def __init__(self, userId, songs):
        """
        Entity that stores a userId and his top 5 songs, used when sending matches to the frontend
        :param userId: the id of the participant
        :param songs: the 5 top songs of the user
        """
        self.userId = userId
        self.songs = songs
