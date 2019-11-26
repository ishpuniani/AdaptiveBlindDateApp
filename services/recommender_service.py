"""
1. Read from mongo and get user models
2. Filter models to get char columns
3. match_score = euc(user_self, user_other) + K * euc(user_ideal, user_other) [lower the better]
4. Match users and save the match score in collection (user_match_scores)
5. Retrieve top 'n' matched users
6. Update user_ideal_scores with swipe (real time)
    ideal_score = ideal_score (+|-) other_user/n
    n = number of swipes
7. Refresh user_match_scores every X minutes
    Compute all scores at X minutes
    TODO:: future scope -> add 'is_modified' flag to user_match_scores and user_ideal_scores

Collections used:
user_model
user_match_scores
user_ideal_scores
"""
import services.utilities as ut
from repository.user_model_repository import UserModelRepository
from repository.user_repository import UserRepository
import json


class RecommenderService:
    __user_model_repository = None
    __user_respository = None

    def __init__(self):
        self.__user_model_repository = UserModelRepository()
        self.__user_repository = UserRepository()

    def get_recommendations(self, public_id):
        user_model_db = self.__user_model_repository.get_all_user_models()
        data_df = ut.json_to_df(user_model_db,
                                columns=['public_id', 'conscientiousness', 'neuroticism', 'agreeableness', 'openness',
                                         'extraversion'])
        user_ideal_model_db = self.__user_model_repository.get_all_ideal_models()

        ideal_df = ut.json_to_df(user_ideal_model_db)
        ideal_df = ideal_df.drop('swipes', axis=1)
        ideal_df = ideal_df.drop('_id', axis=1)
        print("ideal df")

        self_score = ut.calculate_similarity(data_df, data_df)
        ideal_score_a_b = ut.calculate_similarity(data_df, ideal_df)
        ideal_score_b_a = ut.calculate_similarity(ideal_df, data_df)

        # finding match score
        match_score = ut.find_match_score(self_score, ideal_score_a_b, ideal_score_b_a)

        # find n matches for userid with lowest match score
        # userid and number of matches needed, to be fetched from UI
        matches = ut.user_match_score(match_score, userid=public_id)
        final_match_user_list = (matches[public_id].keys())
        ## getting user models for public id
        public_dict = {}
        user_model = self.__user_model_repository.get_user_model(public_id=public_id)
        user_model_name = self.__user_repository.get_user(public_id=public_id,email=None)
        user_model1 = {**user_model, **user_model_name}
        temp_list = []
        ## getting user models for match ids
        for match_id in final_match_user_list:
            match_model = self.__user_model_repository.get_user_model(public_id=match_id)
            match_modelname = self.__user_repository.get_user(public_id=match_id)
            match_model1 = {**match_model, **match_modelname}
            temp_list.append(match_model1)
        value = {'user_model': user_model1,
                 'matches': temp_list}
        #public_dict = json.loads(json.dumps(public_dict))
        return value
