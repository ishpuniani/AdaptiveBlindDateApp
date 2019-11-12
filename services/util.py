import numpy as np


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


def main():
    arr1 = []
    arr2 = []
    euclidean_distance(arr1, arr2)


if __name__ == '__main__':
    main()