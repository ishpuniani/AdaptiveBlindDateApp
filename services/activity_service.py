import json
import requests
import pandas as pd
import argparse
import numpy as np
from pymongo import MongoClient
from services.utilities import *

try:
    # For Python 3.0 and later
    from urllib.parse import quote
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib import quote

API_KEY = 'ygOEqxS2_khcc99_ODjisNpQqAX5JB3pzedPJEJy8UZwdWk7sigevmP8PR_IkbUACZGwX-epxH548ZCWE7VA7p_mbuvlnjD2HFhu2Y4oY8pXeZ06fgC4f6mVmxmnXXYx'

# API constants
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
DEFAULT_LOCATION = 'Dublin'

ACTIVITY_CSV_PATH = '../resources/activity/Activities.csv'
ACTIVITY_MODEL_CSV_PATH = '../resources/activity/activityModel.csv'

client = MongoClient("mongodb+srv://niobrara:niobrara123@adaptiveblinddateapp-hdqaj.mongodb.net/test")
db = client.timble

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--location', dest='location', default=DEFAULT_LOCATION, type=str,
                    help='Search location (default: %(default)s)')
input_values = parser.parse_args()

activities = dict()
activities['Id'] = []
activities['Category'] = []
activities['Name'] = []
activities['Phone'] = []
activities['Imageurl'] = []
activities['Address'] = []
activities['Latitude'] = []
activities['Longitude'] = []
activities['Rating'] = []

categories = ['escapegames', 'diyfood', 'shoppingcenters', 'bikerentals', 'bowling', 'fishing', 'yoga', 'museums',
              'tea', 'golf', 'hiking', 'amusementparks', 'climbing', 'gokarts', 'horsebackriding', 'diners',
              'aquariums', 'beaches', 'arcades', 'movietheaters', 'lakes', 'mini_golf', 'sailing', 'galleries']

char_columns = ['neuroticism','conscientiousness','agreeableness','openness','extraversion']

def request(host, path, url_params=None):
    headers = {'Authorization': 'Bearer %s' % API_KEY, }
    url_params = url_params or {}
    url1 = API_HOST + SEARCH_PATH
    url = url1.format(API_HOST, quote(SEARCH_PATH.encode('utf8')))
    r = requests.request('GET', url, headers=headers, params=url_params)

    return r.json()


def import_activities():
    count = 0
    for l in range(len(categories)):
        url_params = {
            'categories': categories[l],
            'location': input_values.location,
        }
        dictOpenness = request(API_HOST, SEARCH_PATH, url_params=url_params)
        dict2 = dictOpenness.get('businesses')
        dict3 = []

        for i in range(len(dict2)):
            dict3.append(dict2[i]['rating'])
            dict3.sort(reverse=True)
        for i in range(len(dict3)):
            for j in range(len(dict2)):
                if dict2[j]['rating'] == dict3[i] and dict2[j]['name'] not in activities['Name']:
                    dictCategory = dict2[j].get('categories')
                    for k in range(len(dictCategory)):
                        if dict2[j]['categories'][k]['title'] not in activities['Category'] and dict2[j]['categories'][k]['alias'] in categories:
                            activities['Id'].append(count + 1)
                            activities['Category'].append(dict2[j]['categories'][k]['title'])
                            activities['Name'].append(dict2[j]['name'])
                            activities['Phone'].append(dict2[j]['display_phone'])
                            activities['Imageurl'].append(dict2[j]['image_url'])
                            activities['Address'].append(dict2[j]['location']['display_address'])
                            activities['Latitude'].append(dict2[j]['coordinates']['latitude'])
                            activities['Longitude'].append(dict2[j]['coordinates']['longitude'])
                            activities['Rating'].append(dict2[j]['rating'])
                            count += 1

    pd.DataFrame.from_dict(data=activities).to_csv(ACTIVITY_CSV_PATH, header=True, index=False)


def dump_activities():
    replace_collection(db, 'Activities', ACTIVITY_CSV_PATH)
    print('Collection replaced')


def import_and_dump_activities():
    import_activities()
    print('Activities imported')
    dump_activities()


def upload_activity_model(activity_model_path):
    print("Replacing activity model")
    replace_collection(db, 'ActivityModels', activity_model_path)
    print("Activity model replaced")


def get_user_char_array(user_id):
    """
    1. Get users_model from db by id
    2. Convert to array of char
    :param user_id: public_id of user
    :return: array of characteristics
    """
    return []


def match_activities(user_1_id, user_2_id):
    """
    1. Get all activities from db
    2. Get users from db
    3. Iterate over activities and compute scores
    4. Return activity instance with best(least) score
    :param user_1:
    :param user_2:
    :return: matched activity
    """
    user_1_arr = get_user_char_array(user_1_id)
    user_2_arr = get_user_char_array(user_2_id)
    min_score = 10000000.0
    min_activity_id = ''
    for am in db.ActivityModels.find():
        am_arr = json_to_df(am, char_columns)
        score = compute_activity_match_score(user_1_arr, user_2_arr, am)
        if score < min_score:
            min_score = score
            min_activity_id = am['activity_id']

    matched_activity = db.Activities.find_one({'Id':min_activity_id})
    return {'score':min_score, 'activity':matched_activity}


def compute_activity_match_score(user_1, user_2, activity):
    """
    find activity score with users
    score = euc(a*u1, a*u2)
    :param user_1: user1 from match pair characteristic array
    :param user_2: user2 from match pair characteristic arrays
    :param activity: activity characteristic array
    :return:
    """
    score = euclidean_distance(np.multiply(user_1, activity), np.multiply(user_2, activity))
    return score


if __name__ == '__main__':
    # import_and_dump_activities()
    upload_activity_model(ACTIVITY_MODEL_CSV_PATH)

