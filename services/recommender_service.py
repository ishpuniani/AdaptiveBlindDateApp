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
import services.utilities as ut


def main():
    data = {"123":{"n_con":2.0,"conscientiousness":4.0,"n_neu":1.0,"neuroticism":3.0,"n_agr":1.0,"agreeableness":3.0,"n_ope":1.0,"openness":3.0,"n_ext":2.0,"extraversion":4.0},"234":{"n_con":1.0,"conscientiousness":3.0,"n_neu":1.0,"neuroticism":3.0,"n_agr":1.0,"agreeableness":3.0,"n_ope":1.0,"openness":3.0,"n_ext":1.0,"extraversion":3.0},"345":{"n_con":1.0,"conscientiousness":3.0,"n_neu":1.0,"neuroticism":3.0,"n_agr":1.0,"agreeableness":3.0,"n_ope":1.0,"openness":3.0,"n_ext":1.0,"extraversion":3.0},"456":{"n_con":1.0,"conscientiousness":3.0,"n_neu":1.0,"neuroticism":3.0,"n_agr":1.0,"agreeableness":3.0,"n_ope":1.0,"openness":3.0,"n_ext":1.0,"extraversion":3.0},"567":{"n_con":1.0,"conscientiousness":3.0,"n_neu":1.0,"neuroticism":3.0,"n_agr":1.0,"agreeableness":3.0,"n_ope":1.0,"openness":3.0,"n_ext":1.0,"extraversion":3.0}}
    data_df = ut.json_to_df(data,columns=['conscientiousness', 'neuroticism', 'agreeableness', 'openness', 'extraversion'])

    arr1= data_df.loc['123',:].values
    arr2 = data_df.loc['234',:].values
    #print(arr1,arr2)
    res_self = ut.euclidean_distance(arr1,arr2)
    print("self score=",res_self)

    data_ideal = {"123": {"conscientiousness": 6.0, "neuroticism": 6.0, "agreeableness": 6.0, "openness": 6.0, "extraversion": 6.0, "swipes": 4}, "234": {"conscientiousness": 5, "neuroticism": 5, "agreeableness": 5, "openness": 5, "extraversion": 5, "swipes": 6}, "345": {"conscientiousness": 5, "neuroticism": 5, "agreeableness": 5, "openness": 5, "extraversion": 5, "swipes": 8}}
    ideal_df = ut.json_to_df(data_ideal)
    ideal_df = ideal_df.drop('swipes', axis=1)
    #print(ideal_df)

    arr1 = ideal_df.loc['123', :].values
    arr2 = ideal_df.loc['234', :].values
    #print(arr1, arr2)
    res_ideal = ut.euclidean_distance(arr1, arr2)
    print("ideal score=",res_ideal)



if __name__ == '__main__':
    main()