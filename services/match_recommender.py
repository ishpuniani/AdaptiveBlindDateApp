class MatchRecommender:
    __db = None
    def __init__(self, db):
        self.__db = db
    
    def get_recommended_matches(self, user_public_id):
        return db.user.find({public_id: user_public_id})
