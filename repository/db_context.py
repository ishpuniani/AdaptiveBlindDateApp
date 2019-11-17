from pymongo import MongoClient


class DbContext:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if DbContext.__instance is None:
            client = MongoClient('mongodb+srv://niobrara:niobrara123@adaptiveblinddateapp-hdqaj.mongodb.net/test')
            DbContext.__instance = client.timble
        return DbContext.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DbContext.__instance is None:
            raise Exception("This class is a singleton!")
        else:
            DbContext.__instance = self
