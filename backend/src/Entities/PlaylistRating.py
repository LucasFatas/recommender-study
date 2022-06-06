class PlaylistRating:

    def __init__(self, userId, matchedUserId, rating):
        """
        Entity that stores the user id along with the rating provided to one of his match-based recommendations.
        :param userId: id of the participant
        :param matchedUserId: id of the participant he matched with
        :param rating: score provided to that playlist
        """
        self.matchedUserId = matchedUserId
        self.rating = rating
        self.userId = userId

