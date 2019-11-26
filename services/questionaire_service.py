import json
import os
import pandas as pd
from repository.user_model_repository import UserModelRepository
from bson.json_util import dumps
import services.utilities as ut


class QuestionnaireService:
    __user_model_repository = None

    def __init__(self):
        self.__user_model_repository = UserModelRepository()

    @staticmethod
    def get_questions():
        SITE_ROOT = os.path.abspath(os.curdir)
        json_url = os.path.join(
            SITE_ROOT, '..', "resources", "questionnaire.json")
        result = json.load(open(json_url))
        questions = []
        # with open('/resources/questionnaire.json') as json_file:
        #   result = json.load(json_file)

        for key in result:
            questions.append({
                'question_id': key,
                'question_text': result[key]['q'],
                'answer_1_id': result[key]['a1'],
                'answer_2_id': result[key]['a2']})

        return questions

    def build_user_model(self, response_data):
        SITE_ROOT = os.path.abspath(os.curdir)
        json_url = os.path.join(
            SITE_ROOT, '..', "resources", "questionnaire.json")
        q_j = json.load(open(json_url))

        q_df = pd.DataFrame(q_j).T.reset_index().dropna()
        q_df.rename(columns={"index": "qid"}, inplace=True)

        responses_graded = []
        for user in response_data:
            responses_graded.append(self.response(user, q_df))

        user_model = self.__user_model_repository.get_user_model(response_data[0]['user_id'])

        user_df = pd.read_json(dumps(user_model))
        user_df.rename(columns={"public_id": "user_id"}, inplace=True)
        user_df.set_index('user_id', inplace=True)
        user_df.drop(columns=['_id'], inplace=True)
        # user_df.rename(columns={"index": "user_id"}, inplace=True)

        user_df_updated = self.update_scores(responses_graded, user_df)
        user_df_updated.reset_index(inplace=True)
        user_df_updated.rename(columns={"user_id": "public_id"}, inplace=True)

        user_model_to_update = {
            "_id": user_model['_id'],
            "public_id": user_df_updated.public_id[0],
            "n_con": user_df_updated.n_con[0],
            "conscientiousness": user_df_updated.conscientiousness[0],
            "n_neu": user_df_updated.n_neu[0],
            "neuroticism": user_df_updated.neuroticism[0],
            "n_agr": user_df_updated.n_agr[0],
            "agreeableness": user_df_updated.agreeableness[0],
            "n_ope": user_df_updated.n_ope[0],
            "openness": user_df_updated.openness[0],
            "n_ext": user_df_updated.n_ext[0],
            "extraversion": user_df_updated.extraversion[0]
        }

        return self.__user_model_repository.save_user_model(user_model_to_update)

    def update_scores(self, user_res, user_df_updated):
        userid = ""
        user_res = user_res[0]
        for key in user_res:
            if key == 'user_id':  # to get userid
                userid = user_res[key]
                continue
            try:
                response_trait = user_res[key][1]  # name of trait for which record being updated
                response_trait_val = user_res[key][0]  # +1/-1 value of that trait
                n_trait_name = "n_" + response_trait[
                                      0:3]  # name of column indicating n responses submitted for this trait

                # update as: score=score+(marks/no of prev response for this trait)
                user_df_updated.loc[userid, response_trait] += (
                        response_trait_val / user_df_updated.loc[userid, n_trait_name])

                if user_df_updated.loc[userid, response_trait] < 0:  # score shouldn't drop below 0, right!
                    user_df_updated.loc[userid, response_trait] = 0

                user_df_updated.loc[userid, n_trait_name] += 1  # update the n response value for this trait
            except Exception as e:
                print(e)
            return user_df_updated

    def response(self, user_q, q_df):
        user_res = dict()
        for key in user_q:  # to get userid
            if key == 'user_id':
                user_res[key] = user_q[key]
            try:
                meta = list(q_df[q_df.qid == key][['positive', 'type']].iloc[0,
                            :].values)  # to get positive answer and question's trait
                if user_q[key] == meta[0]:  # +1 if response matches to positive answer
                    meta[0] = 1
                else:
                    meta[0] = -1  # otherwise -1

                user_res[key] = meta  # make a new entry for each question in the dict
            except:  # occurs when key not found in question bank eg 'userid'
                pass
        return user_res
