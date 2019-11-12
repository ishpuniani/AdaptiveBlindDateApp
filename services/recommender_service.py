"""
1. Read from mongo and get user models
2. Filter models to get char columns
3. match_score = euc(user_self, user_other) + K * euc(user_ideal, user_other) [lower the better]
4. Match users and save the match score in collection (user_match_scores)
5. Retrieve top 'n' matched users
6. Update user_ideal_scores with swipe (real time)
    ideal_score = ideal_score (+|-) other_user/n
    n = number of swipes
7. Refresh user_match_scores every X minutes
    Compute all scores at X minutes
    TODO:: future scope -> add 'is_modified' flag to user_match_scores and user_ideal_scores

Collections used:
user_model
user_match_scores
user_ideal_scores
"""