# CreditDefaultRisk-DataScience

This repository is the output from a class project for the [INFO-GB.3336 Data Mining for Business Analytics](#data-mining-for-business-analytics-course-description) course at [NYU Stern School of Business](http://www.stern.nyu.edu/) taught by Puneet Batra.  

For this project, we built and tuned several models predicting Home Credit Default Risk, as per the [Kaggle competition](https://www.kaggle.com/c/home-credit-default-risk). 

We found an excellent [Kaggle Kernel](https://www.kaggle.com/willkoehrsen/start-here-a-gentle-introduction) by [Will Koehrsen](https://www.kaggle.com/willkoehrsen) that we generally followed.

**More information about the project, evaluation metrics, etc to come soon!**

## Overview
...
... 
...

## Metrics 
The metric by which the Kaggle competition was judged was the Receiver Operator Characteristic Area Under the Curve (ROC AUC).  Before diving into exactly what this measure means, let's back up and take a look at the purpose of the competition and the importance and cost of different types of error.

The first thing to understand in order to grasp all of the various metrics is the confusion matrix, shown below.  
![Confusion Matrix](https://github.com/osuhomebase/CreditDefaultRisk-DataScience/blob/master/Assets%20For%20Presentation/Images/ConfusionMatrix.png)

Note the results can be broken into four quadrants:
* **True Positives** - In this case, true positives are rows of data where the model correctly predicts a credit default.
* **True Negatives** - Again, in this competition, a true negative is when the model correctly predicts someone who does **not** default. 
* **False Positives** - In this dataset, a False Positive is when someone who does not default is predicted to default.
* **False Negatives** - In this dataset, a False Negative is when somoene who **does** default is predicted not to default.

A lot of times, an easy and effective metric that is used to judge a model is accuracy.  Accuracy is simply defined as the proportion of correctness in a classification system... also as a formula:  
```
True Positive + True Negative                         True Positive + True Negative
-------------------------------    =     --------------------------------------------------------------    
All Records                              (True Postive + True Negative + False Positive + False Negative)
```

Accuracy is a great metric, but it does not tell the whole story.  Imagine a model is built and tested on 10,000 patients who reported cancer like symptoms to their doctor.  A lot of people use this same example on 100 or even 10 tested patients, but I use 10,000 to illustrate the magnitude of the probelm.  Now imagine the model classified patients according to the confusion matrix below:  
![Cancer Confusion Matrix](https://github.com/osuhomebase/CreditDefaultRisk-DataScience/blob/master/Assets%20For%20Presentation/Images/CancerConfusion.png)

In this case the accuracy would be 97%, which would typically be great!  If you look closer at the data, however, the "model" is simply classifying every single patient as not having cancer.  Because cancer is relatively rare, the affect a False Negative has on accuracy metric is minimal.  In reality, however, the actual cost of a False Negative is a lost life, which is obviously a far higher cost than a false positive.  Even with an accuracy of 97%, this model is obviously garbage.

As such, typically when deciding on a by which to judge a model, the data scientist should use an expected value framework to decide which of the above should be minimized.  

Even though insurance companies actually do this, you cannot put a price on loss of life, so expected value is difficult in the cancer case.  In credit default, however, you can put a price on someone who does not pay their mortgage.  Let's assume the average value of a mortgage is $1,000,000.00.  That's a million bucks.  For simplicity, let's also assume that homeowners either default on their first payment or don't default at all, and let's assume all 0% interest loans.  In this case, if a homeowner defaults, the bank loses a million bucks.  


## Data Mining For Business Analytics Course Description
Businesses governments and individuals create massive collections of data as a by-product of their activity. Increasingly data is analyzed systematically to improve decision-making. In many cases automating analytical processes is necessary because of the volume of data and the speed with which data are generated. We will examine how data analytics technologies are used to improve decision-making. We will study the fundamental principles and techniques of mining data and we will examine real-world examples and cases to place data-mining techniques in context	to improve your data-analytic thinking and to illustrate that proper application is as much an art as it is a science. In addition we will work hands on with data mining software. After taking this course you should: Approach business problems data analytically. Think carefully & systematically about whether & how data can improve business performance to make better-informed decisions. Be able to interact competently on business analytics topics. Know the fundamental principles of data science that are the basis for analytics processes algorithms & systems. Understand these well enough to work on data science projects and interact with everyone involved. Envision new opportunities. Have had hands-on experience mining data. Be prepared to follow up on ideas or opportunities that present themselves by performing pilot studies.
