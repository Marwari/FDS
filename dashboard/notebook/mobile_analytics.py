
# coding: utf-8

# In[ ]:


import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns


# In[6]:


df=pd.read_csv('C:\\Users\\Bharat\\PycharmProjects\\Rajasthan Hackathon 4.0\\FDS\\dashboard\\notebook\\mobiledata.csv')


# In[ ]:


plt.subplots(figsize=(12,5))
sns.barplot(df['amount'],df['type'])
plt.title('Graph between jobs and balance')
mobile_result = plt.savefig('dashboard/static/images/mobile_analytics.png')

