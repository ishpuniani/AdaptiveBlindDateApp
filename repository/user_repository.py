from repository.db_context import DbContext


class UserRepository:
    __db = None

    def __init__(self):
        self.__db = DbContext.get_instance()

    def get_user(self, public_id=None, email=None):
        if public_id is not None:
            return self.__db.user.find_one({'public_id': public_id})
        if email is not None:
            return self.__db.user.find_one({'email': email})

    def get_all_users(self):
        return self.__db.user.find({})

    def save_user(self, user):
        user_db = self.get_user(public_id=user['public_id'])
        if user_db is not None:
            self.__db.user.update_one({'public_id': user['public_id']},
                                      {'$set': {'name': user['name'], 'email': user['email'],
                                                'password': user['password'],
                                                'mobile': user['mobile']}})
        else:
            self.__db.user.insert(user)
        return self.get_user(public_id=user['public_id'])

    def delete_user(self, public_id):
        self.__db.user.delete_one({'public_id': public_id})
