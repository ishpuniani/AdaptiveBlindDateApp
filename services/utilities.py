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


def main():
    arr1 = []
    arr2 = []
    euclidean_distance(arr1, arr2)


if __name__ == '__main__':
    main()