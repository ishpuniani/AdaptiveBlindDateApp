from repository.db_context import DbContext


class UserModelRepository:
    __db = None

    def __init__(self):
        self.__db = DbContext.get_instance()

    def get_user_model(self, public_id):
        return self.__db.user_model.find_one({'public_id': public_id})

    def get_all_user_models(self):
        return self.__db.user_model.find({})

    def save_user_model(self, user_model):
        print(user_model)
        user_model_db = self.get_user_model(public_id=user_model['public_id'])
        
        if user_model_db is None:
            self.__db.user_model.insert(user_model)
        else:
            self.__db.user_model.update_one({'public_id': user_model.public_id},
                                            {'$set': user_model})

        return user_model

    def delete_user_model(self, public_id):
        self.__db.user_model.delete_one({'public_id': public_id})
