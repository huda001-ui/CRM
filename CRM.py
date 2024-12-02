#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


engine = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "******",
    database = "crm_sales",
    use_pure = True
)
cur = engine.cursor()


# In[3]:


cur.execute("SELECT * FROM accounts")


# In[4]:


result = cur.fetchall()
df = pd.DataFrame(result)


# In[5]:


query = "SELECT * FROM accounts"


# In[6]:


df = pd.read_sql(query, engine)


# In[7]:


df.to_csv('accounts.csv')


# In[8]:


df = pd.read_csv('accounts.csv')


# In[9]:


df


# In[10]:


cur.execute("SELECT * FROM productss")


# In[11]:


result = cur.fetchall()
df = pd.DataFrame(result)


# In[12]:


query = "SELECT * FROM productss"


# In[13]:


df = pd.read_sql(query, engine)


# In[14]:


df.to_csv('productss.csv')


# In[15]:


df = pd.read_csv('productss.csv')


# In[16]:


df


# In[17]:


cur.execute("SELECT * FROM sales_pipeline")


# In[18]:


result = cur.fetchall()
df = pd.DataFrame(result)


# In[19]:


query = "SELECT * FROM sales_pipeline"


# In[20]:


df = pd.read_sql(query, engine)


# In[21]:


df.to_csv('sales_pipeline.csv')


# In[22]:


df = pd.read_csv('sales_pipeline.csv')


# In[23]:


df


# In[24]:


cur.execute("SELECT * FROM sales_teams")


# In[25]:


result = cur.fetchall()
df = pd.DataFrame(result)


# In[26]:


query = "SELECT * FROM sales_teams"


# In[27]:


df = pd.read_sql(query, engine)


# In[28]:


df.to_csv('sales_teams.csv')


# In[29]:


df = pd.read_csv('sales_teams.csv')


# In[30]:


df


# In[31]:


df = pd.read_csv('accounts.csv')


# In[32]:


df.describe()


# In[33]:


sns.displot(data = df, x = 'revenue', kind = "hist",
           kde = True)


# In[34]:


plt.figure(figsize = (12, 6))
sns.boxplot(x = 'sector', y = 'revenue',
            hue = 'sector', data = df,
           flierprops = dict (markerfacecolor = 'black'))
plt.xlabel('Sector')
plt.ylabel('Revenue')
plt.xticks(rotation = 45)
plt.show()


# In[35]:


plt.figure(figsize = (12, 6))
sns.boxplot(x = 'sector', y = 'employees',
            hue = 'sector', data = df,
           flierprops = dict (markerfacecolor = 'black'))
plt.xlabel('Sector')
plt.ylabel('Employees')
plt.xticks(rotation = 45)
plt.show()


# In[36]:


df = pd.read_csv('productss.csv')
plt.figure(figsize = (6, 4))
sns.barplot(x='product',y='sales_price', data=df, width = 0.8,
           ci = None)
plt.xlabel('Product')
plt.ylabel('Sales Price')
plt.title('Compare Product Prices')
plt.xticks(rotation = 45)
plt.show()


# In[37]:


df = pd.read_csv('sales_pipeline.csv')


# In[38]:


plt.figure(figsize = (15, 6))
sns.histplot( x = 'product', data = df,
    bins = 36)
plt.yticks([])
plt.title('Most Requested Product')
plt.show()


# In[39]:


df1 = pd.read_csv('sales_pipeline.csv')
df2 = pd.read_csv('sales_teams.csv')
merged_df = pd.merge(df1, df2,
                     on = 'sales_agent')
merged_df.to_csv('sales.csv',
                 index = True)


# In[40]:


df = pd.read_csv('sales.csv')
df.head()


# In[41]:


plt.figure(figsize = (20, 7))
df = df.sort_values(by = 'sales_agent',
                   ascending = False)
sns.barplot( x = 'sales_agent', y = 'close_value',
            hue = 'regional_office',palette = 'Blues_r', ci = None,
            data = df)
plt.xticks(rotation = 45)
plt.yticks([])
plt.xlabel('Sales Agent')
plt.ylabel('Sales')
plt.title('Top Selling Sales Agent In Regional Offices')
plt.show()


# In[42]:


plt.figure(figsize = (10, 4))
df['close_date'] = pd.to_datetime(df['close_date'])
df['Year'] = df['close_date'].dt.strftime('%Y-%m')
df = df.sort_values('close_date')
sns.relplot(x = 'Year' , y = 'close_value', data = df, kind = 'line', errorbar = None)
plt.gcf().set_size_inches((10, 4))
plt.tight_layout()
plt.xlabel('Year')
plt.ylabel('Transaction Profits')
plt.title('Deal Profit Trends By Month')
plt.show()

