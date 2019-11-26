import json
import services.activity_service as act
from repository.user_model_repository import UserModelRepository
from repository.user_repository import UserRepository
from repository.matched_user_repository import MatchedUsersRepository
from repository.activity_repository import ActivityRepository
from bson.json_util import dumps

__user_model_repository = UserModelRepository()
__user_repository = UserRepository()
__matched_user_repository = MatchedUsersRepository()
__activity_repository = ActivityRepository()

# user_swipes={"123":[],"234":[],"345":[],"456":[],"567":[],"678":[],"789":[]}
# with open('user_swipes.json', 'w') as outfile:
#     json.dump(user_swipes, outfile)

# get input
input_swipe_data = {"userid": "678", "userid2": "234", 'swipe': 1}  # swipe= +1 / -1


def ideal_score_update(input_swipe_data):
    # update ideal scores based on swipe left/right

    # read ideal score
    with open('user_ideal_score.json') as json_file:
        ui_j = json.load(json_file)

    # read user score
    with open('user_score.json') as json_file:
        uo_j = json.load(json_file)

    userid = input_swipe_data['userid']
    userid2 = input_swipe_data['userid2']
    i_scores = dumps(__user_model_repository.get_user_ideal_model(userid))
    o_scores = dumps(__user_model_repository.get_user_model(userid2))

    i_scores['conscientiousness'] += o_scores['conscientiousness'] * input_swipe_data['swipe'] / i_scores['swipes']
    i_scores['neuroticism'] += o_scores['neuroticism'] * input_swipe_data['swipe'] / i_scores['swipes']
    i_scores['agreeableness'] += o_scores['agreeableness'] * input_swipe_data['swipe'] / i_scores['swipes']
    i_scores['openness'] += o_scores['openness'] * input_swipe_data['swipe'] / i_scores['swipes']
    i_scores['extraversion'] += o_scores['extraversion'] * input_swipe_data['swipe'] / i_scores['swipes']
    i_scores['swipes'] += 1

    __user_model_repository.save_user_ideal_model(i_scores)


def swipe(input_swipe_data):
    # update user like list and return if likebacks
    # read user_swipes
    with open('user_swipes.json', 'r') as json_file:
        user_swipes = json.load(json_file)

    user1 = input_swipe_data["userid"]
    user2 = input_swipe_data["userid2"]

    if user1 not in user_swipes:
        user_swipes[user1] = []

    # update user_swipes
    user_swipes[user1].append(input_swipe_data[user2])
    # remove duplicates
    user_swipes[user1] = list(set(user_swipes[user1]))

    # write to user_swipes
    with open('user_swipes.json', 'w') as outfile:
        json.dump(user_swipes, outfile)

    # check if swiped user like 'em back
    likeback = 1 if user1 in user_swipes[user2] else 0

    ideal_score_update(input_swipe_data)

    # matched_users -> u1, u2, activity
    match_dict = {}
    if likeback == 1:
        matched_activity_id = act.match_activities(user1, user2)
        match_dict = {'user1': user1, 'user2': user2, 'activity_id': matched_activity_id}
        __matched_user_repository.save_matches(match_dict)

    return match_dict


def matches(userId):
    res = []
    matches_arr = __matched_user_repository.get_matches(userId)
    for match in matches_arr:
        us1 = match['user1']
        us2 = match['user2']
        activity_id = match['activity_id']
        us = us1 if us1 != userId else us2
        user2 = dumps(__user_repository.get_user(public_id=us))
        activity = __activity_repository.get_activity(activity_id)
        match_dict = {
            'match_name': user2['name'],
            'match_ph': user2['mobile'],
            'activity_cat': activity['Category'],
            'activity_name': activity['Name'],
            'activity_add': activity['Address'].join(' ')
        }
        res.append(match_dict)
    return res