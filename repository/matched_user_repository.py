from repository.db_context import DbContext
from bson.json_util import dumps


class MatchedUsersRepository:
    __db = None

    def __init__(self):
        self.__db = DbContext.get_instance()

    def save_matches(self, match):
        self.__db.matched_users.insert(match)
        return True

    def get_all_matches(self):
        return dumps(self.__db.matched_users.find({}))

    def get_matches(self, userId):
        return dumps(self.__db.matched_users.find({'$or': [{'user1': userId}, {'user2': userId}]}))
