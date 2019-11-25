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
    #print(data_df)
    l1 = len(data_df)
    data_ideal = {"123": {"conscientiousness": 6.0, "neuroticism": 6.0, "agreeableness": 6.0, "openness": 6.0, "extraversion": 6.0, "swipes": 4}, "234": {"conscientiousness": 5, "neuroticism": 5, "agreeableness": 5, "openness": 5, "extraversion": 5, "swipes": 6}, "345": {"conscientiousness": 5, "neuroticism": 5, "agreeableness": 5, "openness": 5, "extraversion": 5, "swipes": 8}, "456": {"conscientiousness": 5, "neuroticism": 5, "agreeableness": 5, "openness": 5, "extraversion": 5, "swipes": 8},"567": {"conscientiousness": 5, "neuroticism": 5, "agreeableness": 5, "openness": 5, "extraversion": 5, "swipes": 8}}
    ideal_df = ut.json_to_df(data_ideal)
    ideal_df = ideal_df.drop('swipes', axis=1)
    #print(ideal_df)
    self_score = ut.calculate_similarity(data_df,data_df)
    print("self_score =", self_score)
    ideal_score_a_b = ut.calculate_similarity(data_df,ideal_df)
    print("ideal_score_a_b =",ideal_score_a_b)
    ideal_score_b_a = ut.calculate_similarity(ideal_df, data_df)
    print("ideal_score_b_a =", ideal_score_b_a)

    # finding match score
    match_score = ut.find_match_score(self_score,ideal_score_a_b,ideal_score_b_a)
    print("match scores for all users=",match_score)

    # find n matches for userid with lowest match score
    # userid and number of matches needed, to be fetched from UI
    out = ut.user_match_score(match_score)
    print(out)

if __name__ == '__main__':
    main()