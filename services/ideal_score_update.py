#!/usr/bin/env python
# coding: utf-8

# In[2]:

#get input
input_json={'userid':'123','userid2':'234','swipe':1}


# In[28]:


# aa=pd.read_csv('user_ideal_score.csv')
# aa.set_index('userid').T.to_json('user_ideal_score.json')


# In[13]:


import numpy as np
# import pandas as pd
import json


with open('user_ideal_score.json') as json_file:
    ui_j = json.load(json_file)
    
with open('user_score.json') as json_file:
    uo_j = json.load(json_file)
    
userid=input_json['userid']
i_scores=ui_j[userid]
# print(i_scores)
o_scores=uo_j[userid]
# print(o_scores)

i_scores['conscientiousness']+=o_scores['conscientiousness']*input_json['swipe']/i_scores['swipes']
i_scores['neuroticism']+=o_scores['neuroticism']*input_json['swipe']/i_scores['swipes']
i_scores['agreeableness']+=o_scores['agreeableness']*input_json['swipe']/i_scores['swipes']
i_scores['openness']+=o_scores['openness']*input_json['swipe']/i_scores['swipes']
i_scores['extraversion']+=o_scores['extraversion']*input_json['swipe']/i_scores['swipes']
i_scores['swipes']+=1

ui_j[userid]=i_scores
with open('user_ideal_score.json', 'w') as outfile:
    json.dump(ui_j, outfile)


# In[9]:





# In[10]:




