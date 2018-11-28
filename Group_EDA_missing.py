#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:24:57 2018

@author: tinghao
"""

import pandas as pd
import numpy as np



train = pd.read_csv('train_v1.csv')



# calculate the percentage of missing value
missing_perc= train.isnull().sum() * 100 / len(train)
missing_perc= pd.DataFrame(missing_perc).reset_index()
missing_perc.columns= ['columns','percentage']


# replace missing value (I can't come up a better idea about how to fill in missing values)
train = train.fillna(train.median())

# Training data extreme values/outliers cleaning 
train['AMT_INCOME_TOTAL']=np.where(train['AMT_INCOME_TOTAL']>100000000,np.nan,train['AMT_INCOME_TOTAL']) 
train = train.drop('FLAG_PHONE',axis = 1)
train = train[train['REGION_RATING_CLIENT_W_CITY'] != (-1)]
train = train.drop('FONDKAPREMONT_MODE',axis=1) # too much missing values, not information, not worth the effort
train['OBS_30_CNT_SOCIAL_CIRCLE'] = np.where(train['OBS_30_CNT_SOCIAL_CIRCLE']>100,np.nan,train['OBS_30_CNT_SOCIAL_CIRCLE'])
train['OBS_60_CNT_SOCIAL_CIRCLE'] = np.where(train['OBS_60_CNT_SOCIAL_CIRCLE']>100,np.nan,train['OBS_60_CNT_SOCIAL_CIRCLE'])
train['AMT_REQ_CREDIT_BUREAU_QRT'] = np.where(train['AMT_REQ_CREDIT_BUREAU_QRT']>100,np.nan,train['AMT_REQ_CREDIT_BUREAU_QRT'])


train.to_csv('train_v2_clean.csv',index=False)









