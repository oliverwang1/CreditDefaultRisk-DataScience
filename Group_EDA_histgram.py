#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 13:19:31 2018

@author: xuzifan
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#read data
train = pd.read_csv('application_train.csv')
train['TARGET'].astype(int).plot.hist()


#fill in the missing values with median
train = train.fillna(train.median())


#clean and transform variables
train['DAYS_BIRTH']=-train['DAYS_BIRTH']/365

train['DAYS_EMPLOYED']=abs(np.where(train['DAYS_EMPLOYED']==365243,np.nan,train['DAYS_EMPLOYED']))#365243 is an outlier
train['DAYS_EMPLOYED']=train['DAYS_EMPLOYED']/365
train['DAYS_REGISTRATION']=-train['DAYS_REGISTRATION']/365
train['DAYS_ID_PUBLISH']=-train['DAYS_ID_PUBLISH']/365
train['DAYS_LAST_PHONE_CHANGE']=-train['DAYS_LAST_PHONE_CHANGE']/365


#kde function (for numeric variable)
def kde_target(var_name, df):
    
    # Calculate the correlation coefficient between the variable and the target
    corr = df['TARGET'].corr(df[var_name])
    
    # Calculate medians for repaid vs not repaid
    avg_repaid = df.ix[df['TARGET'] == 0, var_name].median()
    avg_not_repaid = df.ix[df['TARGET'] == 1, var_name].median()
    
    plt.figure(figsize = (12, 6))
    
    # Plot the distribution for target == 0 and target == 1
    sns.kdeplot(df.ix[df['TARGET'] == 0, var_name], label = 'TARGET == 0')
    sns.kdeplot(df.ix[df['TARGET'] == 1, var_name], label = 'TARGET == 1')
    
    # label the plot
    plt.xlabel(var_name); plt.ylabel('Density'); plt.title('%s Distribution' % var_name)
    plt.legend();
    
    # print out the correlation
    print('The correlation between %s and the TARGET is %0.4f' % (var_name, corr))
    # Print out average values
    print('Median value for loan that was not repaid = %0.4f' % avg_not_repaid)
    print('Median value for loan that was repaid =     %0.4f' % avg_repaid)


#countplot funtion (for categorical variable)
def countplot_x(var_name,df):
 sns.countplot(x=var_name, hue="TARGET", data=df)


def countplot_y(var_name,df):
 sns.countplot(y=var_name, hue="TARGET", data=df)
    

#hisrgram function
def hist(var_name, df):
   # Set the style of plots
   plt.style.use('fivethirtyeight')

   # Plot the distribution of ages in years
   plt.hist(df[var_name], edgecolor = 'k', bins=20)
   plt.title('%s Distribution' % var_name); plt.xlabel(var_name); plt.ylabel('Count');

    

#plot for the categorical variables
countplot_x('NAME_CONTRACT_TYPE',train)
countplot_x('CODE_GENDER',train)
countplot_x('FLAG_OWN_CAR', train)
countplot_x('CNT_CHILDREN', train)
countplot_x('NAME_TYPE_SUITE',train)
countplot_y('NAME_INCOME_TYPE', train)
countplot_y('NAME_EDUCATION_TYPE',train)
countplot_x('NAME_FAMILY_STATUS',train)
countplot_x('NAME_HOUSING_TYPE',train)
countplot_y('OCCUPATION_TYPE',train)
countplot_y('CNT_FAM_MEMBERS',train)
countplot_x('WEEKDAY_APPR_PROCESS_START',train)
countplot_y('ORGANIZATION_TYPE',train) #how to figure out a better layout



#plot for the numeric variables
hist('AMT_INCOME_TOTAL', train)#some problem need to be fixed
hist('AMT_CREDIT', train)
hist('AMT_ANNUITY',train)
hist('AMT_GOODS_PRICE',train)
hist('DAYS_BIRTH',train)
hist('DAYS_EMPLOYED',train)#it needs to be remove abnormal values(done at line 26)
hist('DAYS_REGISTRATION',train)
hist('DAYS_ID_PUBLISH',train)
hist('DAYS_LAST_PHONE_CHANGE',train)





