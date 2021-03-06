# CreditDefaultRisk-DataScience

This repository is the output from a class project for the [INFO-GB.3336 Data Mining for Business Analytics](#data-mining-for-business-analytics-course-description) course at [NYU Stern School of Business](http://www.stern.nyu.edu/) taught by Puneet Batra.  

For this project, we built and tuned several models predicting Home Credit Default Risk, as per the [Kaggle competition](https://www.kaggle.com/c/home-credit-default-risk). 

We found an excellent [Kaggle Kernel](https://www.kaggle.com/willkoehrsen/start-here-a-gentle-introduction) by [Will Koehrsen](https://www.kaggle.com/willkoehrsen) that we generally followed.

**More information about the project, evaluation metrics, etc to come soon!**

## Overview

Home Credit Group is a leading international multi-channel provider of consumer finance founded in the Czech Republic in 1997, with operations on 3 continents. As a company, they've completed more than 131 million loans for people worldwide and employ more than 120,000 full time employees. Home Credit Group is a world leader of financing, operating in over 365,000 global distribution points of sale.

It strives to broaden financial inclusion for the unbanked population by providing a positive and safe borrowing experience. In order to make sure this underserved population has a positive loan experience, Home Credit makes use of a variety of alternative data--including telco and transactional information--to predict their clients' repayment abilities.

While Home Credit is currently using various statistical and machine learning methods to make these predictions, they're challenging Kagglers to help them unlock the full potential of their data. Our project is all about the whole competition and using the models to predict the default risk by the datasets they provides.

We seperate our project into four parts: Introduction, exploratory data analysis, feature engineering and implementation.

In introduction, we are going through the structrure of project and metrices overview, then we are getting know more about the dataset: missing values, the distribution of important features, the correlation and mutual information between the features and target variable and figure out the outlies. after doing the exploratory data analysis, we are going to transform the data for the models: encoding the category features, generate polynomial feature and domain knowledge features. after feature engineering, we will use logistic regression, decision tree and random forests to build models for predicting.


## Metrics 
The metric by which the Kaggle competition was judged was the Receiver Operator Characteristic Area Under the Curve (ROC AUC).  Before diving into exactly what this measure means, let's back up and take a look at the purpose of the competition and the importance and cost of different types of error.

The first thing to understand in order to grasp all of the various metrics is the confusion matrix, shown below.  The confusion matrix represents the outcome of the experiment.  It is a sum of results by correctness, broken into four quadrants.

* **True Positives (TP)** - In this case, true positives are rows of data where the model correctly predicts a credit default.
* **True Negatives (TN)** - Again, in this competition, a true negative is when the model correctly predicts someone who does **not** default. 
* **False Positives (FP)** - In this dataset, a False Positive is when someone who does not default is predicted to default.
* **False Negatives (FN)** - In this dataset, a False Negative is when somoene who **does** default is predicted not to default.
![Confusion Matrix](https://github.com/osuhomebase/CreditDefaultRisk-DataScience/blob/master/Assets%20For%20Presentation/Images/ConfusionMatrix.png)


Once we have the confusion matrix as a starting point, the outcome of an experiment can be judged.  A lot of times, an easy and effective metric that is used to judge a model based on data from the matrix is accuracy.  Accuracy is simply defined as the proportion of correctness in a classification system... also as a formula:  
```
True Positive + True Negative                         True Positive + True Negative
-------------------------------    =     --------------------------------------------------------------    
All Records                              (True Postive + True Negative + False Positive + False Negative)
```

Accuracy is a great metric, but it does not tell the whole story.  Imagine a model is built and tested on 10,000 patients who reported cancer like symptoms to their doctor.  A lot of people use this same example on 100 or even 10 tested patients, but I use 10,000 to illustrate the magnitude of the probelm.  Now imagine the model classified patients according to the confusion matrix below:  
![Cancer Confusion Matrix](https://github.com/osuhomebase/CreditDefaultRisk-DataScience/blob/master/Assets%20For%20Presentation/Images/CancerConfusion.png)

In this case the accuracy would be 97%, which would typically be great!  If you look closer at the data, however, the "model" is simply classifying every single patient as not having cancer.  Because cancer is relatively rare, the affect a False Negative has on accuracy metric is minimal.  In reality, however, the actual cost of a False Negative is a lost life, which is obviously a far higher cost than a false positive.  Even with an accuracy of 97%, this model is obviously garbage.

As such, typically when deciding on a metric by which to judge a model, the data scientist should use an expected value framework to decide which of the above should be minimized.  

Even though insurance companies actually do this, you cannot put a price on loss of life, so expected value is difficult in the cancer case.  In credit default, however, you can put a price on someone who does not pay their mortgage.  Let's assume the average value of a mortgage is $1,000,000.00.  That's a million bucks.   
![Austin Powers](https://github.com/osuhomebase/CreditDefaultRisk-DataScience/blob/master/Assets%20For%20Presentation/Images/one-million-dollars.jpg)  
For simplicity, let's also assume that homeowners either default on their first payment or don't default at all, and let's assume all 0% interest loans.  If we used the same logic as above, one possible confusion matrix would look like the one below:  
![Credit Default Confusion Matrix](https://github.com/osuhomebase/CreditDefaultRisk-DataScience/blob/master/Assets%20For%20Presentation/Images/CreditDefaultAccuracy.png)  
This model predicts 90% accuracy, but if a homeowner defaults, the bank loses a million bucks.  This is obviously horrible for the bank.  The bank would rather predict that all mortgages will fail and not loan anyone any money.  This would be horrible for everyone else, and I can tell you from experience, it kind of did suck immediately following the financial crash of 2008 when banks overcompensated for handing out loans like Halloween candy during the boom.  The Confusion Matrix would look like the one below:  
![All Default Confusion Matrix](https://github.com/osuhomebase/CreditDefaultRisk-DataScience/blob/master/Assets%20For%20Presentation/Images/all-default.png)  
OK fine, let's say the average mortgage is still $1,00,000.00, but the homeowner pays the bank a flat $250,000.00 fee for each mortgage.  So a **False Negative** still ***costs*** the bank $1,000,000.00, but a **True Negative** ***earns*** the bank $250,000.00.  This is pretty close to reality.  If the bank is like any business and exists for the purpose of profit maximization, the most important metric should be one that ***minimizes False Negatives*** while simultaneously ***maximizes True Negatives***.  If you look at it in terms of opportunity cost, you may also want to *minimize* False Positives as well just thinking about what could have been.

Anyway, let's pretend a model now comes up with the following:  
![Expected Value Confusion Matrix](https://github.com/osuhomebase/CreditDefaultRisk-DataScience/blob/master/Assets%20For%20Presentation/Images/ExpectedValueMatrix.png)  
The above matrix has the exact same accuracy as the previous credit default confusion matrix, but if you look at expected value, rather than earning nothing, you get the following:
```
$250,000 * 50 True Negative - $1,000,000 * 1 False Positive = $11,500,000.00
```
Two other metrics that get tossed around are **precision** and **recall.**  There's a [good article](https://towardsdatascience.com/beyond-accuracy-precision-and-recall-3da06bea9f6c) on precision and recall that does a better job of defining both than I can, but I'll copy some text and paraphrase a bit here.
> **Precision,** expresses the proportion of the data points our model says was relevant actually were relevant.
or in a formula:  
```
                        true positives                        Credit Defaults Correctly Identified
Precision     =       ------------------            =        ---------------------------------------
                  true positives + false positives      Correctly Identified + Incorrectly Labeled as Default
```

> **Recall,** also known as **True Positive Rate,** or **Sensitivity** expresses the ability to find all relevant instances in a dataset  
```
                        true positives                           Credit Defaults Correctly Identified
Recall         =      -----------------------        =         ---------------------------------------
                  true positives + false negatives         Correctly Identified + Incorrectly as No Default
```
The intuitive metric to use in our case would be to maximize recall, also known as True Positive Rate.  It's the proportion of default cases that we found out of all the default cases that actually existed.  This is especially a good metric when looking at ***imbalanced classification problems,*** which are problems where the overwhelming majority of data points are one classification, in our case no default.  In the image below, we outline from the training data the distribution of defaults (1) vs non-defaults (0) clearly heavily favors those who do not default on their mortgage.  There's roughly an 8% default rate (24,825 defaults / 307,511 total records)

![Target Distribution](https://github.com/osuhomebase/CreditDefaultRisk-DataScience/blob/master/Assets%20For%20Presentation/Images/TargetDistribution.png)  

The only problem with this is if we predict that every single person in the population will default, then our recall becomes 1.0!  This is the same problem we had with accuracy, and creates the same profit maximization issue as before.

Precision is even less useful.  If we changed the model slightly and correctly identified even a single credit default, the precision would be 1.0, but the recall would be very low.  There's a problem that increasing precision decreases recall and vice-versa.  In our model, as in a lot of situations, we want to find the optimal blend of precision and recall.  

One option to find this optimal blend is the F1 score, which calculates the harmonic mean of precision and recall.
```
                         precision * recall
  F1 Score       =  2 * ---------------------
                         precision + recall
```

So the F1 score seems like a really good metric to use, why then did the competition use this other score called the ROC AUC?  If only the interwebs provided answers to questions like this, and not just [entitled d-bags huffing with non-answers to questions](https://stats.stackexchange.com/questions/210700/how-to-choose-between-roc-auc-and-f1-score) that innocent people ask on Stack Overflow.

Oh, sorry, I digress.  The problem with F1 is it is a bit of a black box and hard to decipher without additional context.  F1 is based on a single confusion matrix given a specific threshold, but who is to say that threshold is the best?  As [Stuart Reynolds](https://www.quora.com/What-does-it-mean-to-have-high-AUC-but-low-F1-score) put it:
> People who publish F1 scores (or accuracies, or precisions, or any measure derived from a confusion matrix) willfully without further context, are charlatans and deserve to be strapped to Elon Musk’s next rocket (preferably the part that comes back down and explodes).   

Reynolds does a good job explaining F1 vs AUC. The ROC AUC stands for Reciever Operating Characteristics Area Under the Curve.  Once again, [someone explains it better than we can](https://towardsdatascience.com/understanding-auc-roc-curve-68b2303cc9c5), but we'll quote and paraphrase again. Similar to F1, the AUROC attempts to balance inversely proportional metrics.  AUROC still uses recall (True Positive Rate), but balances it against the **False Positive Rate.**
```
                         FP
False Positive Rate =  --------
                        TN+FP
```
Further, the AUROC measures the True Postive Rate vs the False Positive Rate ***at different thresholds.***  Threshold means the probability at which an observation is considered positive or negative.  So this obviously only works for probabalistic classifications.  
![Receiver Operating Characteristics](https://www.statisticshowto.datasciencecentral.com/wp-content/uploads/2016/08/ROC-curve.png)  

My man Will Koehrsen says explains his own chart above best:  
>A single line on the graph indicates the curve for a single model, and movement along a line indicates changing the threshold used for classifying a positive instance. The threshold starts at 0 in the upper right to and goes to 1 in the lower left. A curve that is to the left and above another curve indicates a better model. For example, the blue model is better than the red model, which is better than the black diagonal line which indicates a naive random guessing model.  

AUROC seems like a good metric for something like a Kaggle competition where the objective is to build a very generalized model that is the best at various thresholds, but in real life, it really means nothing out of context.  An actual bank would be required to estimate expected value to make sound business decisions so that is exactly what we will do.  

## Expected Value as a Metric  





## Data Mining For Business Analytics Course Description
Businesses governments and individuals create massive collections of data as a by-product of their activity. Increasingly data is analyzed systematically to improve decision-making. In many cases automating analytical processes is necessary because of the volume of data and the speed with which data are generated. We will examine how data analytics technologies are used to improve decision-making. We will study the fundamental principles and techniques of mining data and we will examine real-world examples and cases to place data-mining techniques in context	to improve your data-analytic thinking and to illustrate that proper application is as much an art as it is a science. In addition we will work hands on with data mining software. After taking this course you should: Approach business problems data analytically. Think carefully & systematically about whether & how data can improve business performance to make better-informed decisions. Be able to interact competently on business analytics topics. Know the fundamental principles of data science that are the basis for analytics processes algorithms & systems. Understand these well enough to work on data science projects and interact with everyone involved. Envision new opportunities. Have had hands-on experience mining data. Be prepared to follow up on ideas or opportunities that present themselves by performing pilot studies.
