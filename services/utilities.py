import json
import numpy as np
import pandas as pd
from collections import OrderedDict
from itertools import islice
from bson.json_util import dumps

def euclidean_distance(arr1, arr2):
    """
    Used by recommender system to find similarity between
    1. users
    2. activity and user
    :param arr1: first array
    :param arr2: second array
    :return: Finding the euclidean distance (RMSE) between 2 arrays
    """
    d = np.linalg.norm(np.subtract(arr1, arr2))
    return d

#@staticmethod
def json_to_df(json1, columns=None):
    """
    Helper function for converting json to Dataframe
    :param json: Json to be converted to Dataframe
    :param columns: Columns to be added to Dataframe
    :return: Corresponding Dataframe for given json
    """

    json1 = dumps(json1)
    json1 = json.loads(json1)
    df = pd.DataFrame(json1)
        #df1 = df.T.copy()
    print("here")
        # df.rename(columns={"index":"id"},inplace=True)
        # df = pd.DataFrame(json).T.reset_index()
    if columns is not None:
        print("in if")
        df = df.loc[:, df.columns.str.contains('|'.join(columns))]
    return df



def calculate_similarity(data_df, ideal_df):
    """
    Calculates how similar or dissimilar all pair of users are with each other. This forms
    an n*n matrix
    :param data_df: Similarity between users based on their individual personalities fetched from
    user models generated for each of them
    :param ideal_df: Similarity between users based based on their "required" personalities in a partner fetched from
    user models generated for each of them
    :return: Similarity scores ( euclidian distance)
    """
    score_dict = {}
    l1 = len(data_df)
    for i in range(l1):
        arr1 = ideal_df.iloc[i, 1:].values
        user_id_1 = ideal_df['public_id'][i]
        score_other_list = []
        score_dict[user_id_1] = {}
        # print(score_dict)
        for j in range(l1):
            user_id_2 = data_df['public_id'][j]
            # print(user_id_1,user_id_2)
            if (i == j):
                continue
            arr2 = data_df.iloc[j, 1:].values
            # score_other_list.append(euclidean_distance(arr1, arr2))
            score_dict[user_id_1][user_id_2] = euclidean_distance(arr1, arr2)
            # print(score_dict)
    # del score_dict[user_id_1]
    return score_dict


def find_match_score(self_score, ideal_score_a_b, ideal_score_b_a):
    """
    Aggregates all 3 similarity scores to generate match score for each users
    :param self_score: Similarity between users based on their individual personalities fetched from
    user models generated for each of them
    :param ideal_score_a_b: Similarity between users based based on their "required" personalities in a partner fetched from
    user models generated for each of them
    :param ideal_score_b_a: Similarity between users based based on their "required" personalities in a partner fetched from
    user models generated for each of them
    :return: Aggregated match score for each user with every other user
    """
    # finding match score
    match_score = {}
    for user1 in self_score:
        m = 100
        match_score[user1] = {}
        for user2 in self_score[user1]:
            av_score = ((self_score[user1][user2] + ideal_score_a_b[user1][user2] + ideal_score_b_a[user1][user2]) // 3)
            if (av_score <= m):
                m = av_score
            match_score[user1][user2] = m
    # print(match_score)
    return match_score


def user_match_score(match_score=None, userid='234', n=5):
    """ Finds 'n' best matched users for a user id according to the match score

    :param match_score: dictionary containing all the match scores for all users
    :param userid: the user for whom best matches are supposed to be found
    :param n: Number of best matches required
    :return: 'n' best matched partners for given userid
    """
    matches = {}
    if userid in match_score:
        vals = match_score[userid]
        # print(vals)
        match_ascending = OrderedDict(sorted(vals.items(), key=lambda kv: kv[1]))
        # print(match_ascending)
        get_sorted_response = dict((x, y) for x, y in list(
            islice(OrderedDict(sorted(match_score[userid].items(), key=lambda kv: kv[1])).items(), n)))
        # print(get_sorted_response)
        matches[userid] = get_sorted_response
        return matches


def replace_collection(db, collection_name, filepath):
    db_cm = db[collection_name]
    dataset = pd.read_csv(filepath)
    data_json = json.loads(dataset.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)


def main():
    arr1 = []
    arr2 = []
    euclidean_distance(arr1, arr2)


if __name__ == '__main__':
    main()
