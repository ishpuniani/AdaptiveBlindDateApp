#!/usr/bin/env python
# coding: utf-8

# In[1]:

#get input
with open('user_response.json') as json_file:
    response_data = json.load(json_file)



import numpy as np
import pandas as pd
import json


# In[2]:


# q_df=pd.read_csv('questionnaire.csv',engine='python')
# q_df.dropna(inplace=True)


# In[3]:


# q_df.drop(columns=['Orig_q']).set_index('qid').T.to_json('questionnaire.json')


# ### get questtionaire 

# In[4]:


with open('questionnaire.json') as json_file:
    q_j = json.load(json_file)

q_df=pd.DataFrame(q_j).T.reset_index().dropna()
q_df.rename(columns={"index":"qid"},inplace=True)
q_df.head()


# ### get user response (at runtime, obtained from front end) 

# In[5]:



# In[6]:




# ### get response and decide +1 or -1 for each question

# In[7]:


def response(user_q):
    user_res=dict()
    for key in user_q: # to get userid
        if key=='userid':
            user_res[key]=user_q[key]
        try: 
            meta=list(q_df[q_df.qid==key][['positive','type']].iloc[0,:].values) # to get positive answer and question's trait
            if user_q[key]==meta[0]: # +1 if response matches to positive answer
                meta[0]=1
            else:
                meta[0]=-1 # otherwise -1

            user_res[key]=meta # make a new entry for each question in the dict
        except: # occurs when key not found in question bank eg 'userid'
            pass
    return user_res


# In[8]:


responses_graded=[]
for user in response_data:
    responses_graded.append(response(user))    


# In[9]:


responses_graded


# ### read existing user score 

# In[10]:


# user_df=pd.read_csv('user_scores.csv')


# In[11]:


# user_df.set_index('userid').T.to_json('user_score.json')

with open('user_score.json') as json_file:
    u_j = json.load(json_file)

user_df=pd.DataFrame(u_j).T.reset_index().dropna()
user_df.rename(columns={"index":"userid"},inplace=True)
user_df.head()


# ### update user score 

# In[12]:


user_df_updated=user_df.copy()


# In[13]:


def update_scores(user_res):
    for key in user_res:
#         userid=0
        global user_df_updated
        if key=='userid': # to get userid
            userid=user_res[key]
#             print(userid)
            continue
        try:
            # make default row if user not present already
            if userid not in user_df_updated.index.values:
                a=pd.Series(name=userid,data={"n_con":1,"conscientiousness":3,"n_neu":1,
                                         "neuroticism":3,"n_agr":1,"agreeableness":3,"n_ope":1,"openness":3,"n_ext":1,"extraversion":3})
                user_df_updated=user_df_updated.append(a)
                
            response_trait=user_res[key][1] # name of trait for which record being updated
            response_trait_val=user_res[key][0] # +1/-1 value of that trait
            n_trait_name="n_"+response_trait[0:3] # name of column indicating n responses submitted for this trait 
            
            # update as: score=score+(marks/no of prev response for this trait)
            user_df_updated.loc[userid,response_trait]+=(response_trait_val/user_df_updated.loc[userid,n_trait_name])
            
            if user_df_updated.loc[userid,response_trait]<0: # score shouldn't drop below 0, right!
                user_df_updated.loc[userid,response_trait]=0
                
            user_df_updated.loc[userid,n_trait_name]+=1 # update the n response value for this trait
        except Exception as e: print(e)


# In[14]:


user_df_updated.set_index('userid', inplace=True)
for user_res in responses_graded:
    update_scores(user_res)
user_df_updated.reset_index(inplace=True)


# In[15]:


user_df_updated


# In[16]:


user_df_updated.set_index('userid').T.to_json('user_score.json')

