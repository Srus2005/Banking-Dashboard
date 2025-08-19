#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[6]:


df = pd.read_csv('C:/Users/srush/OneDrive/Desktop/Banking Project/Banking.csv')
df.head(5)


# In[6]:


df.shape


# In[8]:


df.info()


# In[9]:


# Generate descriptive statistics for the dataframe
df.describe()


# In[14]:


bins = [0, 100000, 300000, float('inf')]
labels= ['Low', 'Med', 'High']

df['Income Band'] = pd.cut(df['Estimated Income'], bins=bins, labels=labels, right=False)


# In[36]:


df['Income Band'].value_counts().plot(kind='bar')


# In[37]:


# Examine the distribution of unique categories in categorical columns
categorical_cols = df[["BRId", "GenderId","IAId", "Amount of Credit Cards", "Nationality", "Occupation", "Fee Structure", "Loyalty Classification", "Properties Owned", "Risk Weighting", "Income Band"]].columns

for col in categorical_cols:
    print(f"Value Counts for '{col}':")
    display(df[col].value_counts())


# # Bivariate Analysis

# In[33]:


for i, predictor in enumerate(df[["BRId", "GenderId","IAId", "Amount of Credit Cards", "Nationality", "Occupation", "Fee Structure", "Loyalty Classification", "Properties Owned", "Risk Weighting", "Income Band"]].columns):
    plt.figure(i)
    sns.countplot(data=df, x=predictor, hue='GenderId')


# 

# # Univariate Analysis

# In[35]:


for i, predictor in enumerate(df[["BRId", "GenderId","IAId", "Amount of Credit Cards", "Nationality", "Occupation", "Fee Structure", "Loyalty Classification", "Properties Owned", "Risk Weighting", "Income Band"]].columns):
    plt.figure(i)
    sns.countplot(data=df, x=predictor)


# In[38]:


for i, predictor in enumerate(df[["BRId", "GenderId","IAId", "Amount of Credit Cards", "Nationality", "Occupation", "Fee Structure", "Loyalty Classification", "Properties Owned", "Risk Weighting", "Income Band"]].columns):
    plt.figure(i)
    sns.countplot(data=df, x=predictor, hue='Nationality')


# In[39]:


# Histplot of value counts for different occupation

for col in categorical_cols:
    if col == "Occupation":
        continue
    plt.figure(figsize=(8,4))
    sns.histplot(df[col])
    plt.title('Histogram of Occupation Count')
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.show()


# # Numerical Analysis

# In[8]:


numerical_cols = ['Estimated Income', 'Superannuation Savings', 'Credit Card Balance', 'Bank Loans', 'Bank Deposits', 'Checking Accounts', 'Saving Accounts', 'Foreign Currency Account', 'Business Lending']

# Univariate analysis and visualization
plt.figure(figsize=(15,15))
for i, col in enumerate(numerical_cols):
    plt.subplot(4,3,i+1)
    sns.histplot(df[col],kde= True)
    plt.title(col)
plt.show()


# # Heatmaps

# In[45]:


numerical_cols = ['Estimated Income', 'Superannuation Savings', 'Credit Card Balance', 'Bank Loans', 'Bank Deposits', 'Checking Accounts', 'Saving Accounts', 'Foreign Currency Account', 'Business Lending']

correlation_matrix = df[numerical_cols].corr()

plt.figure(figsize=(12,12))
sns.heatmap(correlation_matrix, annot= True, cmap='crest', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()


# In[ ]:




