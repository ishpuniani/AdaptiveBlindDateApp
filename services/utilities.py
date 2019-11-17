import numpy as np
import pandas as pd


def euclidean_distance(arr1, arr2):
    """
    Used by recommender system to find similarity between
    1. users
    2. activity and user
    :param arr1: first array
    :param arr2: second array
    :return: Finding the euclidean distance (RMSE) between 2 arrays
    """
    d = np.linalg.norm(np.subtract(arr1,arr2))
    return d


def json_to_df(json, columns=None):
    df = pd.DataFrame(json).T
    # df.rename(columns={"index":"id"},inplace=True)
    # df = pd.DataFrame(json).T.reset_index()
    if columns is not None:
        df = df.loc[:, df.columns.str.contains('|'.join(columns))]
    return df

def calculate_similarity(data_df,ideal_df):
    score_dict ={}
    l1 = len(data_df)
    for i in range(l1):
        arr1 = ideal_df.iloc[i, :].values
        user_id_1 = ideal_df.index[i]
        score_other_list = []
        score_dict[user_id_1] = {}
        #print(score_dict)
        for j in range(l1):
            user_id_2 = data_df.index[j]
            #print(user_id_1,user_id_2)
            if (i==j):
                continue
            arr2 = data_df.iloc[j, :].values
            #score_other_list.append(euclidean_distance(arr1, arr2))
            score_dict[user_id_1][user_id_2] = euclidean_distance(arr1, arr2)
            #print(score_dict)
    #del score_dict[user_id_1]
    return score_dict


def find_match_score(self_score, ideal_score_a_b,ideal_score_b_a):
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
    #print(match_score)
    return match_score

from collections import OrderedDict
from itertools import islice
def user_match_score(match_score = None,userid='234',n=4):
    """ Fetches the user id

    :param match_score:
    :param userid:
    :param n:
    :return:
    """
    matches = {}
    if userid in match_score:
        vals = match_score[userid]
        #print(vals)
        match_ascending = OrderedDict(sorted(vals.items(), key=lambda kv: kv[1]))
        #print(match_ascending)
        get_sorted_response = dict((x, y) for x,y in list(islice(OrderedDict(sorted(match_score[userid].items(), key=lambda kv: kv[1])).items(),n)))
        #print(get_sorted_response)
        matches[userid] = get_sorted_response
        return matches


def main():
    arr1 = []
    arr2 = []
    euclidean_distance(arr1, arr2)


if __name__ == '__main__':
    main()