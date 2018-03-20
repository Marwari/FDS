
# coding: utf-8

# In[1]:


import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from sklearn import preprocessing, cross_validation, neighbors ,svm
import seaborn as sns
import pickle

df = pd.read_csv('C:\\Users\\Bharat\\PycharmProjects\\Rajasthan Hackathon 4.0\\FDS\\dashboard\\notebook\\Credit_Card.csv')
df=df[["LIMIT_BAL","SEX","EDUCATION","MARRIAGE","AGE","PAY_0","PAY_2","PAY_3","PAY_4","PAY_5","PAY_6","BILL_AMT1","BILL_AMT2","BILL_AMT3","BILL_AMT4","BILL_AMT5","BILL_AMT6","PAY_AMT1","PAY_AMT2","PAY_AMT3","PAY_AMT4","PAY_AMT5","PAY_AMT6","default.payment.next.month"]]


# In[3]:


plt.subplots(figsize=(12,5))
sns.barplot(df['AGE'],df['LIMIT_BAL'])
plt.title('Graph between age and balance')
creditcard_result = plt.savefig('dashboard/static/images/creditcard_analytics.png')

