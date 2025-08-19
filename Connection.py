#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mysql-connector-python


# In[2]:


import mysql.connector
import pandas as pd

# Connect to server
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Srushti10@")


# In[3]:


query = "SELECT*FROM banking_case.customer"


# In[4]:


df = pd.read_sql(query,cnx)


# In[5]:


cnx.close()


# In[6]:


df.head(5)


# In[ ]:




