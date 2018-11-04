#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 13:19:31 2018

@author: xuzifan
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#read data
train = pd.read_csv('application_train.csv')
train['TARGET'].astype(int).plot.hist()


#fill in the missing values with median
train = train.fillna(train.median())


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
   plt.hist(df[var_name], edgecolor = 'k')
   plt.title('%s Distribution' % var_name); plt.xlabel(var_name); plt.ylabel('Count');

    








