import json
import numpy as np

# user_swipes={"123":[],"234":[],"345":[],"456":[],"567":[],"678":[],"789":[]}
# with open('user_swipes.json', 'w') as outfile:
#     json.dump(user_swipes, outfile)

# get input
input_swipe_data={"userid":"678","userid2":"234",'swipe':1} # swipe= +1 / -1

    
    
# update ideal scores based on swipe left/right

with open('user_ideal_score.json') as json_file:
    ui_j = json.load(json_file)
    
with open('user_score.json') as json_file:
    uo_j = json.load(json_file)
    
userid=input_swipe_data['userid']
i_scores=ui_j[userid]
# print(i_scores)
o_scores=uo_j[userid]
# print(o_scores)

i_scores['conscientiousness']+=o_scores['conscientiousness']*input_swipe_data['swipe']/i_scores['swipes']
i_scores['neuroticism']+=o_scores['neuroticism']*input_swipe_data['swipe']/i_scores['swipes']
i_scores['agreeableness']+=o_scores['agreeableness']*input_swipe_data['swipe']/i_scores['swipes']
i_scores['openness']+=o_scores['openness']*input_swipe_data['swipe']/i_scores['swipes']
i_scores['extraversion']+=o_scores['extraversion']*input_swipe_data['swipe']/i_scores['swipes']
i_scores['swipes']+=1

ui_j[userid]=i_scores
with open('user_ideal_score.json', 'w') as outfile:
    json.dump(ui_j, outfile)
    
    

# update user like list and return if likebacks
def swipe(input_swipe_data):
    
    with open('user_swipes.json','r') as json_file:
        user_swipes = json.load(json_file)

    # update user_swipes
    user_swipes[input_swipe_data["userid"]].append(input_swipe_data["userid2"])
    # remove duplicates
    user_swipes[input_swipe_data["userid"]]=list(set(user_swipes[input_swipe_data["userid"]]))

    with open('user_swipes.json', 'w') as outfile:
        json.dump(user_swipes, outfile)

    # check if swiped user like 'em back
    likeback=1 if input_swipe_data["userid"] in user_swipes[input_swipe_data["userid2"]]  else 0

    return likeback

if input_swipe_data['swipe']==1:
    swipe(input_swipe_data)
    