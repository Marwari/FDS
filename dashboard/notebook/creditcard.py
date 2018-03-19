
# coding: utf-8

# In[38]:

import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, neighbors ,svm
import pickle

df = pd.read_csv('C:\\Users\\Bharat\\PycharmProjects\\Rajasthan Hackathon 4.0\\FDS\\dashboard\\notebook\\Credit_Card.csv')
df=df[["LIMIT_BAL","SEX","EDUCATION","MARRIAGE","AGE","PAY_0","PAY_2","PAY_3","PAY_4","PAY_5","PAY_6","BILL_AMT1","BILL_AMT2","BILL_AMT3","BILL_AMT4","BILL_AMT5","BILL_AMT6","PAY_AMT1","PAY_AMT2","PAY_AMT3","PAY_AMT4","PAY_AMT5","PAY_AMT6","default.payment.next.month"]]
df.head()

def credit_model():
    global df
    y = df[["default.payment.next.month"]]
    x = df.drop(["default.payment.next.month"],1)
    x = x.values
    y = y.values
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(x,y, test_size=0.2)
    clf = svm.SVC()
    clf.fit(X_train, y_train)
    with open('creditcard.pickle','wb') as f:
        pickle.dump(clf,f)
    pickle_in=open('creditcard.pickle','rb')
    clf=pickle.load(pickle_in)
    accuracy = clf.score(X_test, y_test)
    print(accuracy)
    return clf
# In[42]:

# c=clf.predict([[120000,2,2,2,26,-1,2,0,0,0,2,2682,1725,2682,3272,3455,3261,0,1000,1000,1000,0,2000]])
# print(c)



