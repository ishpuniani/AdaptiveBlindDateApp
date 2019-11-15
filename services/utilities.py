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
        score_other_list = []
        for j in range(i + 1, l1):
            arr2 = data_df.iloc[j, :].values
            score_other_list.append(euclidean_distance(arr1, arr2))
        score_dict[i] = score_other_list
    del score_dict[i]
    return score_dict

def find_match_score(self_score,ideal_score):
    # finding match score
    match_score = {}
    # fetch individual scores and minimize them
    temp, temp1 = 0, 0
    l1 = len(self_score)
    for i in range(l1):
        temp = self_score[i]
        temp1 = ideal_score[i]
        temp_list = []
        for j in range(len(temp)):
            temp_list.append(((temp[j] + temp1[j]) // 2))
            m = max(temp_list)
            # storing the maximum match score and indices for it
        match_score[i] = [m, [x for x, y in enumerate(temp_list) if y == m]]
        # print(temp_list)
    return match_score

def main():
    arr1 = []
    arr2 = []
    euclidean_distance(arr1, arr2)


if __name__ == '__main__':
    main()