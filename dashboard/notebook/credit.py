# coding: utf-8

# In[1]:

from dashboard import views
import pandas as pd
import numpy as np


from sklearn import cross_validation, svm

df = pd.read_csv('C:\\Users\\Bharat\\PycharmProjects\\Rajasthan Hackathon 4.0\\FDS\\dashboard\\notebook\\Credit_Card.csv')
print(df.head())


def handle_non_numerical_data(df):
    columns = df.columns.values

    for column in columns:
        text_digit_vals = {}

        def convert_to_int(val):
            return text_digit_vals[val]

        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 1
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x += 1
            df[column] = list(map(convert_to_int, df[column]))
            print("done")
    return df


df = handle_non_numerical_data(df)

def model():
    global df
    # df = df.drop(["ID"], 1)
    df.head()
    y = df[["default.payment.next.month"]]
    x = df.drop(["default.payment.next.month"], 1)
    x = x.values
    y = y.values
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.2)
    clf = svm.SVC()
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)
    print(accuracy)
    return clf
