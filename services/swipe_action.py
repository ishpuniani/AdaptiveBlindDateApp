import json

# get input
input_swipe_data={"userid":"234","swiped_userid":"567"}

def swipe(input_swipe_data):
    
    with open('user_swipes.json','r') as json_file:
        user_swipes = json.load(json_file)

    # update user_swipes
    user_swipes[input_swipe_data["userid"]].append(input_swipe_data["swiped_userid"])
    # remove duplicates
    user_swipes[input_swipe_data["userid"]]=list(set(user_swipes[input_swipe_data["userid"]]))

    with open('user_swipes.json', 'w') as outfile:
        json.dump(user_swipes, outfile)

    # check if swiped user like 'em back
    likeback=1 if input_swipe_data["userid"] in user_swipes[input_swipe_data["swiped_userid"]]  else 0

    return likeback

# output- 1 for likeback , 0 for not
swipe(input_swipe_data)