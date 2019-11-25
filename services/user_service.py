from repository.user_repository import UserRepository


class UserService:
    __user_repository = None

    def __init__(self):
        self.__user_repository = UserRepository()

    def get_user(self, public_id=None, email=None):
        if public_id is not None:
            return self.__user_repository.get_user(public_id=public_id)
        if email is not None:
            return self.__user_repository.get_user(email=email)

    def get_all_users(self):
        return self.__user_repository.get_all_users()

    def save_user(self, user):
        return self.__user_repository.save_user(user=user)

    def delete_user(self, public_id):
        self.__user_repository.delete_user(public_id=public_id)
