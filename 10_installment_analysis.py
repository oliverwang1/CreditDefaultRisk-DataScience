#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 17:09:26 2018

@author: xuzifan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('application_train_v3_clean.csv')

install = pd.read_csv('installments_payments.csv')


#2D scatter 的标准code
def scatter2d(feature_1,feature_2,df):
    ax1=plt.subplot(211)

    plt.scatter(df.loc[df['TARGET'] == 0, feature_1],
                df.loc[df['TARGET'] == 0, feature_2], color='g',s = 5)
    plt.xlabel(feature_1)
    plt.ylabel(feature_2)
    
    plt.subplot(212,sharex=ax1)

    plt.scatter(df.loc[df['TARGET'] == 1, feature_1],
                df.loc[df['TARGET'] == 1, feature_2], color='r',s = 5)
    plt.xlabel(feature_1)
    plt.ylabel(feature_2)
    plt.show()
    
 
    
def kde_target(var_name, df):
    
    # Calculate the correlation coefficient between the new variable and the target
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

## 请check下这个file和install analysis，然后得出共同的feature，注意可能有bug，你之前是做了异常值处理的
## 请务必细心

# Replace some outliers
install.loc[install['NUM_INSTALMENT_VERSION'] > 70, 'NUM_INSTALMENT_VERSION'] = np.nan
install.loc[install['DAYS_ENTRY_PAYMENT'] < -4000, 'DAYS_ENTRY_PAYMENT'] = np.nan
    


# Some new features
#实际付款天 减去 需要付款天
install['DAYS_ENTRY_PAYMENT - DAYS_INSTALMENT'] = install['DAYS_ENTRY_PAYMENT'] - install['DAYS_INSTALMENT']

#分期金额 减去 实付金额
install['AMT_INSTALMENT - AMT_PAYMENT'] = install['AMT_INSTALMENT'] - install['AMT_PAYMENT']

#实付金额 处于 分期金额
install['AMT_PAYMENT / AMT_INSTALMENT'] = install['AMT_PAYMENT'] / install['AMT_INSTALMENT']
 


#calculate how many previous loans does a person have
#how many installments does a previous loan have
count = install.groupby(['SK_ID_CURR','SK_ID_PREV']).size()
count = pd.DataFrame(count.groupby(level=[0]).size()).reset_index().rename(columns={'SK_ID_CURR':'SK_ID_CURR',0:'frequency'})
install = pd.merge(install,count, on='SK_ID_CURR', how='inner')



#calculate the total amount of the previous loans of each person
previous = pd.DataFrame(install.groupby('SK_ID_CURR')['DAYS_INSTALMENT'].sum()).reset_index()
train = pd.merge(train, previous, on='SK_ID_CURR', how='inner')
train['percentage']=abs(train['DAYS_INSTALMENT']/train['AMT_CREDIT'])
perc=train.loc[:,['SK_ID_CURR','percentage']]
install = pd.merge(install,perc, on='SK_ID_CURR', how='outer')



#check the default status of every SK_ID_CURR
install['payback_days']=install['DAYS_ENTRY_PAYMENT']-install['DAYS_INSTALMENT']
install['install_left'] = install['AMT_INSTALMENT']-install['AMT_PAYMENT']

install['default']=np.where((install['payback_days']<=0) & (install['install_left']<=0),0,1)

defaultrate=pd.DataFrame(install.groupby('SK_ID_CURR')['default'].mean()).reset_index()
defaultrate.columns = ['SK_ID_CURR','defaultrate']
install = pd.merge(install,defaultrate, on='SK_ID_CURR', how='outer')


#### 为了保证合并data的时候sk_id_curr的值是unique的，所以在install的维度必须把每个
#currentid的值取mean，run 出来如果结果不理解，这一部分可以改成取median.
one = install.groupby('SK_ID_CURR')['DAYS_ENTRY_PAYMENT - DAYS_INSTALMENT'].mean()
two = install.groupby('SK_ID_CURR')['AMT_INSTALMENT - AMT_PAYMENT'].mean()
three = install.groupby('SK_ID_CURR')['AMT_PAYMENT / AMT_INSTALMENT'].mean()


train_1 = train.loc[:,['SK_ID_CURR','TARGET']]

install_features= pd.concat([one,two,three, train_1],axis= 1)

kde_target('DAYS_ENTRY_PAYMENT - DAYS_INSTALMENT', install_features)
kde_target('AMT_INSTALMENT - AMT_PAYMENT', install_features)
kde_target('AMT_PAYMENT / AMT_INSTALMENT', install_features)

scatter2d('DAYS_ENTRY_PAYMENT - DAYS_INSTALMENT','DAYS_ENTRY_PAYMENT',install)


new_features= ['SK_ID_CURR','frequency', 'percentage','defaultrate']
newinstall = install[new_features].groupby('SK_ID_CURR').mean()#为什么这样分组算平均值里面的percentage会有nan
new_install= pd.concat([newinstall, train_1],axis= 1)


kde_target('frequency', new_install)
kde_target('percentage', new_install)
kde_target('defaultrate', new_install)




install_features_2= pd.concat([install_features,newinstall],axis = 1)


install_features_2.to_csv("Install_Features.csv",index=False)
    









