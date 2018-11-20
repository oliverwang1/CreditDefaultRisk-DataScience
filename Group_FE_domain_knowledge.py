#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 09:45:48 2018

@author: xuzifan
"""

# pandas for data manipulation

import pandas as pd 
import numpy as np


#reading data 
data = pd.read_csv('train_v3_encoded.csv')
data= data.iloc[:,1:]
#nomalize features
#data['DAYS_BIRTH']=data['DAYS_BIRTH']*(-1)/365
#data['DAYS_EMPLOYED']=data['DAYS_EMPLOYED'].replace(365243,data['DAYS_EMPLOYED'].median())
#data['DAYS_EMPLOYED']=data['DAYS_EMPLOYED']*(-1)/365


#replace missing data with median for every column
data = data.fillna(data.median())



# domain knowledge features
data['CREDIT_INCOME_PERCENT'] = data['AMT_CREDIT'] / data['AMT_INCOME_TOTAL']
data['ANNUITY_INCOME_PERCENT'] = data['AMT_ANNUITY'] /data['AMT_INCOME_TOTAL']
data['CREDIT_TERM'] = data['AMT_ANNUITY'] /data['AMT_CREDIT']
data['DAYS_EMPLOYED_PERCENT'] = data['DAYS_EMPLOYED'] / data['DAYS_BIRTH']
data['GENDER_CAR']= data['CODE_GENDER']*data['FLAG_OWN_CAR']
data['TERM']=data['AMT_CREDIT']/data['AMT_ANNUITY']


# feature transform: transform every feature to new form which similiar to normal 
# distribution (normal distribution will be better perform in modeling)

data['AMT_INCOME_TOTAL_1']=np.log1p(data['AMT_INCOME_TOTAL'])

data['AMT_CREDIT_1']=np.log1p(data['AMT_CREDIT'])

data['AMT_ANNUITY_1']=np.log1p(data['AMT_ANNUITY'])

data['AMT_GOODS_PRICE_1']=np.log1p(data['AMT_GOODS_PRICE'])

data['APARTMENTS_AVG_1'] = np.log1p(50*data['APARTMENTS_AVG']) 

data['YEARS_BEGINEXPLUATATION_AVG_1']=(data['YEARS_BEGINEXPLUATATION_AVG'])**30

data['YEARS_BUILD_AVG_1']=(data['YEARS_BUILD_AVG'])**3

data['COMMONAREA_AVG_1']=(data['COMMONAREA_AVG'])**(-1/200)

data['ELEVATORS_AVG_1']=(data['ELEVATORS_AVG'])**(1/40)

data['ENTRANCES_AVG_1']=(data['ENTRANCES_AVG'])**(1/3)

data['FLOORSMAX_AVG_1']=(data['FLOORSMAX_AVG'])**(1/2.5)

data['FLOORSMIN_AVG_1']=(data['FLOORSMIN_AVG'])**(1/2.2)

data['LANDAREA_AVG_1']=(data['LANDAREA_AVG'])**(1/5)

data['LIVINGAPARTMENTS_AVG_1']=(data['LIVINGAPARTMENTS_AVG'])**(1/3)

data['LIVINGAREA_AVG_1']=(data['LIVINGAREA_AVG'])**(1/3.5)

data['NONLIVINGAPARTMENTS_AVG_1']=(data['NONLIVINGAPARTMENTS_AVG'])**(1/7)

data['NONLIVINGAREA_AVG_1']=(data['NONLIVINGAREA_AVG'])**(1/5)

data['TOTALAREA_MODE_1']=(data['TOTALAREA_MODE'])**(1/3)

data['OBS_30_CNT_SOCIAL_CIRCLE_1']=(data['OBS_30_CNT_SOCIAL_CIRCLE'])**(1/7)

data['DEF_30_CNT_SOCIAL_CIRCLE_1']=(data['DEF_30_CNT_SOCIAL_CIRCLE'])**(1/7)

data['OBS_60_CNT_SOCIAL_CIRCLE_1']=(data['OBS_60_CNT_SOCIAL_CIRCLE'])**(1/7)

data['DEF_60_CNT_SOCIAL_CIRCLE_1']=(data['DEF_60_CNT_SOCIAL_CIRCLE'])**(1/7)







# more new features: select the features below to put in models afterwards

data['earn_average']=data['AMT_INCOME_TOTAL_1']/(data['CNT_FAM_MEMBERS']+1)


data['earn_child_average']=data['AMT_INCOME_TOTAL_1']/(data['CNT_CHILDREN']+1)


data['earn_child_fam']= data['AMT_INCOME_TOTAL_1']*(data['CNT_CHILDREN']/(data['CNT_FAM_MEMBERS']+1))


data['house_average']= data['AMT_INCOME_TOTAL_1']/(data['NAME_HOUSING_TYPE']+1)


data['car_realty']=(data['FLAG_OWN_CAR']+data['FLAG_OWN_REALTY'])*data['AMT_INCOME_TOTAL_1']


data['income_employed']=data['AMT_INCOME_TOTAL_1']/data['DAYS_EMPLOYED']


data['income_birth']= data['AMT_INCOME_TOTAL_1']/data['DAYS_BIRTH']


data['income_accompany']=data['AMT_INCOME_TOTAL_1']/(1+data['NAME_TYPE_SUITE'])


data['income_type']=data['AMT_INCOME_TOTAL_1']/(1+data['NAME_INCOME_TYPE'])


data['income_education']=data['AMT_INCOME_TOTAL_1']/(1+data['NAME_EDUCATION_TYPE'])


data['income_famstatus']=data['AMT_INCOME_TOTAL_1']/(1+data['NAME_FAMILY_STATUS']+data['NAME_HOUSING_TYPE'])


data['income_rating']=data['AMT_INCOME_TOTAL_1']/(data['REGION_RATING_CLIENT'])


data['income_ratingcity']=data['AMT_INCOME_TOTAL_1']/(data['REGION_RATING_CLIENT_W_CITY'])


data['income_OBS_30']=data['AMT_INCOME_TOTAL_1']/(1+data['OBS_30_CNT_SOCIAL_CIRCLE_1'])


data['income_DEF_30']=data['AMT_INCOME_TOTAL_1']/(1+data['DEF_30_CNT_SOCIAL_CIRCLE_1'])


data['income_OBS_60']=data['AMT_INCOME_TOTAL_1']/(1+data['OBS_60_CNT_SOCIAL_CIRCLE_1'])


data['income_DEF_60']=data['AMT_INCOME_TOTAL_1']/(1+data['DEF_60_CNT_SOCIAL_CIRCLE_1'])


data['income_obs']=data['AMT_INCOME_TOTAL_1']/(1+data['OBS_30_CNT_SOCIAL_CIRCLE_1']+data['OBS_60_CNT_SOCIAL_CIRCLE_1'])


data['income_def']=data['AMT_INCOME_TOTAL_1']/(1+data['DEF_30_CNT_SOCIAL_CIRCLE_1']+data['DEF_60_CNT_SOCIAL_CIRCLE_1'])


data['income_changephone']=data['AMT_INCOME_TOTAL_1']/(1+data['DAYS_LAST_PHONE_CHANGE'])


data['income_month']=data['AMT_INCOME_TOTAL_1']/(1+data['AMT_REQ_CREDIT_BUREAU_MON'])


data['income_qrt']=data['AMT_INCOME_TOTAL_1']/(1+data['AMT_REQ_CREDIT_BUREAU_QRT'])


data['income_year']=data['AMT_INCOME_TOTAL_1']/(1+data['AMT_REQ_CREDIT_BUREAU_YEAR'])


data['income_total']=data['AMT_INCOME_TOTAL_1']/(1+data['AMT_REQ_CREDIT_BUREAU_DAY']+
     data['AMT_REQ_CREDIT_BUREAU_WEEK']+data['AMT_REQ_CREDIT_BUREAU_MON']+data['AMT_REQ_CREDIT_BUREAU_QRT']+
     data['AMT_REQ_CREDIT_BUREAU_YEAR'])


data['age_child']=data['DAYS_BIRTH']*(data['CNT_CHILDREN']/(1+data['CNT_FAM_MEMBERS']))


data['age_fam']=data['DAYS_BIRTH']/(1+data['CNT_FAM_MEMBERS'])


data['birth_employ']=data['DAYS_BIRTH']/data['DAYS_EMPLOYED']


data['employed_child']=data['DAYS_EMPLOYED']/(1+data['CNT_CHILDREN'])


data['credit_employ']=data['AMT_CREDIT_1']/data['DAYS_EMPLOYED']


data['good_percenrage']=data['AMT_INCOME_TOTAL_1']*(data['AMT_GOODS_PRICE_1']/data['AMT_CREDIT_1'])


data['income_term']=data['AMT_INCOME_TOTAL_1']/(data['AMT_CREDIT_1']/data['AMT_ANNUITY_1'])


data['good_term']=data['AMT_GOODS_PRICE_1']/(data['AMT_CREDIT_1']/data['AMT_ANNUITY_1'])


data['income_credit']=data['AMT_INCOME_TOTAL_1']/data['AMT_CREDIT_1']


data['income_annuity']=data['AMT_INCOME_TOTAL_1']/data['AMT_ANNUITY_1']


data['credit_child_average']=data['AMT_ANNUITY_1']/(data['CNT_CHILDREN']+1)


data['annuity_birth']= data['AMT_ANNUITY_1']/data['DAYS_BIRTH']


data['annuity_accompany']=data['AMT_ANNUITY_1']/(1+data['NAME_TYPE_SUITE'])


data['annuity_type']=data['AMT_ANNUITY_1']/(1+data['NAME_INCOME_TYPE'])


data['annuity_education']=data['AMT_ANNUITY_1']/(1+data['NAME_EDUCATION_TYPE'])


data['annuity_famstatus']=data['AMT_ANNUITY_1']/(1+data['NAME_FAMILY_STATUS']+data['NAME_HOUSING_TYPE'])


data['credit_OBS_30']=data['AMT_CREDIT_1']/(1+data['OBS_30_CNT_SOCIAL_CIRCLE_1'])


data['credit_OBS_60']=data['AMT_CREDIT_1']/(1+data['OBS_60_CNT_SOCIAL_CIRCLE_1'])


data['credit_changephone']=data['AMT_CREDIT_1']/(1+data['DAYS_LAST_PHONE_CHANGE'])


data = pd.read_csv('train_v4.csv')





