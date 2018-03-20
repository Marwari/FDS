
# coding: utf-8

# In[30]:

import pandas as pd
import numpy as np
from sklearn import cross_validation,svm

df = pd.read_csv('C:\\Users\\Bharat\\PycharmProjects\\Rajasthan Hackathon 4.0\\FDS\\dashboard\\notebook\\mobiledata.csv')
df=df[['step','type','amount','nameOrig','oldbalanceOrg','newbalanceOrig','nameDest','oldbalanceDest','newbalanceDest','isFraud','isFlaggedFraud']]
df.dropna(inplace=True)

def handle_non_numerical_data(df):
    columns = df.columns.values
    
    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]
        
        if df[column].dtype != np.int64 :
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 1
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x+=1
            df[column] = list(map(convert_to_int, df[column]))
    
    return df

df = handle_non_numerical_data(df)
print(df.head())



def mobile_model():
    global df
    y = df[['isFraud']]
    x = df.drop(['isFraud'],1)
    x = x.values
    y = y.values
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y, test_size=0.2)
    df.head()

    clf = svm.SVC()
    clf.fit(x_train, y_train)
    accuracy=clf.score(x_test,y_test)
    print(accuracy)
    return clf

# c=clf.predict([[1,1,1000,7865944,133,144,101699,0,0,1]])
# print(c)