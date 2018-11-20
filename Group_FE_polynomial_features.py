#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 22:05:00 2018

@author: xuzifan
"""


import pandas as pd 




data = pd.read_csv('train_v4.csv')

# Polynomial features
data['EXT_SOURCE_2^2'] = data['EXT_SOURCE_2']**2
data['EXT_SOURCE_2^3'] = data['EXT_SOURCE_2']**3
data['EXT_SOURCE_3^2'] = data['EXT_SOURCE_3']**2
data['EXT_SOURCE_3^3'] = data['EXT_SOURCE_3']**3
data['DAYS_BIRTH^2'] = data['DAYS_BIRTH']**2
data['EXT_SOURCE_2 DAYS_BIRTH'] = data['EXT_SOURCE_2'] * data['DAYS_BIRTH']
data['EXT_SOURCE_2^2 DAYS_BIRTH'] = data['EXT_SOURCE_2^2'] * data['DAYS_BIRTH']
data['EXT_SOURCE_3 DAYS_BIRTH'] = data['EXT_SOURCE_3'] * data['DAYS_BIRTH']
data['EXT_SOURCE_3^2 DAYS_BIRTH'] = data['EXT_SOURCE_3^2'] * data['DAYS_BIRTH']
data['EXT_SOURCE_3 DAYS_BIRTH^2'] = data['EXT_SOURCE_3'] * data['DAYS_BIRTH']**2


# Polynomial features
data['DAYS_ID_PUBLISH DAYS_LAST_PHONE_CHANGE'] = data['DAYS_ID_PUBLISH'] * data['DAYS_LAST_PHONE_CHANGE']
data['DAYS_REGISTRATION DAYS_ID_PUBLISH'] = data['DAYS_REGISTRATION'] * data['DAYS_ID_PUBLISH']
data['DAYS_REGISTRATION DAYS_LAST_PHONE_CHANGE'] = data['DAYS_REGISTRATION'] * data['DAYS_LAST_PHONE_CHANGE']
data['DAYS_ID_PUBLISH^2']=data['DAYS_ID_PUBLISH']**2
data['DAYS_REGISTRATION DAYS_ID_PUBLISH DAYS_LAST_PHONE_CHANGE']= data['DAYS_REGISTRATION']*data['DAYS_ID_PUBLISH']*data['DAYS_LAST_PHONE_CHANGE']
data['DAYS_ID_PUBLISH^2 DAYS_LAST_PHONE_CHANGE']=data['DAYS_LAST_PHONE_CHANGE']*data['DAYS_ID_PUBLISH']**2
data['DAYS_REGISTRATION DAYS_ID_PUBLISH^2']=data['DAYS_REGISTRATION']*data['DAYS_ID_PUBLISH']**2



data.to_csv('train_v5_clean_polynomial_features.csv',index=False)








