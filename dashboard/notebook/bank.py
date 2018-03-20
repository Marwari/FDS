import pandas as pd
import numpy as np
from sklearn import cross_validation,svm
df = pd.read_csv('C:\\Users\\Bharat\\PycharmProjects\\Rajasthan Hackathon 4.0\\FDS\\dashboard\\notebook\\bank.csv', delimiter=";")

print(df.head())

df = df[['age', 'job', 'marital', 'education', 'balance','housing', 'loan', 'duration', 'campaign', 'pdays', 'previous', 'poutcome', 'y']]

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
                    x+=1
            df[column] = list(map(convert_to_int, df[column]))
    return df

df = handle_non_numerical_data(df)
def bank_model():
    global df
    X = np.array(df.drop(['loan'], 1))
    y = np.array(df['loan'])
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y, test_size=0.2)
    clf = svm.SVC()
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)
    print(accuracy)
    return clf

