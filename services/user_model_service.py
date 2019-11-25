from repository.user_model_repository import UserModelRepository


class UserModelService:
    __user_model_repository = None

    def __init__(self):
        self.__user_model_repository = UserModelRepository()

    def save_user_default_model(self, public_id):
        user_model = {'public_id': public_id,
                      "n_con": 1, "conscientiousness": 5, "n_neu": 1, "neuroticism": 5, "n_agr": 1, "agreeableness": 5,
                      "n_ope": 1, "openness": 5, "n_ext": 1, "extraversion": 5}
        self.__user_model_repository.save_user_model(user_model)

    def save_user_ideal_model(self, public_id):
        user_ideal_model = {'public_id': public_id,
                            "conscientiousness": 5, "neuroticism": 5, "agreeableness": 5,
                            "openness": 5, "extraversion": 5, "swipes": 1}
        self.__user_model_repository.save_user_ideal_model(user_ideal_model)

    def save_user_model(self, user_model):
        return self.__user_model_repository.save_user_model(user_model=user_model)

    def delete_user_model(self, public_id):
        return self.delete_user_model(public_id=public_id)
