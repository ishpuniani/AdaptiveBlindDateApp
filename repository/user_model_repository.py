from repository.db_context import DbContext


class UserModelRepository:
    __db = None

    def __init__(self):
        self.__db = DbContext.get_instance()

    def get_user_model(self, public_id):
        return self.__db.user_model.find_one({'public_id': public_id})

    def get_user_ideal_model(self, public_id):
        return self.__db.user_ideal_model.find_one({'public_id': public_id})

    def get_all_user_models(self):
        return self.__db.user_model.find({})

    def get_all_ideal_models(self):
        return self.__db.user_ideal_model.find({})

    def save_user_model(self, user_model):
        user_model_db = self.get_user_model(public_id=user_model['public_id'])

        if not user_model_db:
            self.__db.user_model.insert(user_model)
        else:
            self.__db.user_model.update_one({'public_id': user_model['public_id']},
                                                {'$set': user_model})

        return user_model

    def delete_user_model(self, public_id):
        self.__db.user_model.delete_one({'public_id': public_id})

    def save_user_ideal_model(self, user_ideal_model):
        user_ideal_model_db = self.get_user_ideal_model(public_id=user_ideal_model['public_id'])

        if not user_ideal_model_db:
            self.__db.user_ideal_model.insert(user_ideal_model)
        else:
            self.__db.user_ideal_model.update_one({'public_id': user_ideal_model['public_id']},
                                                  {'$set': user_ideal_model})

        return user_ideal_model

    def delete_user_ideal_model(self, public_id):
        self.__db.user_ideal_model.delete_one({'public_id': public_id})
