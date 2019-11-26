from repository.db_context import DbContext
from bson.json_util import dumps


class ActivityRepository:
    __db = None

    def __init__(self):
        self.__db = DbContext.get_instance()

    def get_activity_model(self, activity_id):
        return self.__db.ActivityModels.find_one({'activity_id': activity_id})

    def get_activity(self, id):
        return self.__db.Activities.find_one({'Id': id})

    def get_all_activity_models(self):
        return list(self.__db.ActivityModels.find({}))
