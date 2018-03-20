
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


df = pd.read_csv('C:\\Users\\Bharat\\PycharmProjects\\Rajasthan Hackathon 4.0\FDS\\dashboard\\notebook\\bank.csv', delimiter=";")

df = df[['age', 'job', 'marital', 'education', 'balance','housing', 'loan', 'duration', 'poutcome','y']]


plt.subplots(figsize=(12,5))
sns.barplot(df['job'],df['balance'])
plt.title('Graph between jobs and balance')
result = plt.savefig('dashboard/static/images/analytics.png')