#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 16:23:55 2018

@author: xuzifan
"""

import pandas as pd

# read training data 
# first edition
data = pd.read_csv("Application_train.csv")



# select all the categorical features in training data
categorical_features = ['NAME_CONTRACT_TYPE','CODE_GENDER','FLAG_OWN_CAR','FLAG_OWN_REALTY','NAME_TYPE_SUITE',
                        'NAME_INCOME_TYPE','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS','NAME_HOUSING_TYPE',
                        'OCCUPATION_TYPE','HOUSETYPE_MODE','WALLSMATERIAL_MODE','EMERGENCYSTATE_MODE',
                        'ORGANIZATION_TYPE','WEEKDAY_APPR_PROCESS_START']




"""calculate the default rate of each category in categorical features"""

# create a dataframe 
res = pd.DataFrame(columns=['Unique Values','Default Rate','Total'])

# use for loop to iterate calculation of default rate and add them in the new dataframe
for c in categorical_features:
    norm=data[data['TARGET']==0].groupby([c]).size()
    defau=data[data['TARGET']==1].groupby([c]).size()
    total= pd.concat([defau,norm],axis=1).fillna(0)
    total.columns=['defau','norm']
    
    defau_rate=total.defau.div(total.sum(axis=1))
    
    temp = pd.concat([defau_rate,total.sum(axis=1)],axis=1).reset_index()
    
    temp.columns = ['Unique Values','Default Rate','Total']
    res=res.append(temp)
    
    print("the current feature is: {}".format(c))
    
res.to_csv("categorical data analysis.csv",index=False)



"""encode the categorical features"""

# read the categroy decoding file 
input_encoding = pd.read_csv("categorydecode.csv")

# encoding process
for c in categorical_features:
    
    # create a dictionary for encoding
    dic_features = ['UniqueValues','RiskRanks']

    encoding_number = input_encoding[input_encoding['Features']==c][dic_features]
    encoding_dict =encoding_number.set_index('UniqueValues').T.to_dict('records')
    
    data[c] = data[c].map(encoding_dict[0])
    
    print("the current feature is: {}".format(c))


# save data 
# second edition
data.to_csv("train_v3_encoded.csv",index=False)

