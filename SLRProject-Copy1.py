#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
url = "sales.csv"
df=pd.read_csv(url, header=None)
df


# In[5]:


matplotlib inline


# In[6]:


print(df.shape)


# In[7]:


print(df.head())


# In[8]:


print(df.tail())


# In[9]:


df.columns={"sales","advertising"}
print(df.head())
print(df.info())


# In[10]:


print(df.describe())


# In[11]:


x=df["sales"].values
y=df["advertising"].values
x
y


# In[12]:


plt.scatter(x,y, color='black',label = "Scatter Plot")
plt.title("Relationship between sales and advertising")
plt.xlabel("sales")
plt.ylabel("advertising")
plt.legend(loc=4)
plt.show()


# In[13]:


print(x.shape)
print(y.shape)


# In[14]:


x=x.reshape(-1,1)
y=y.reshape(-1,1)
x.shape


# In[15]:


y.shape


# In[16]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33, random_state=42)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)


# In[17]:


from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(x_train,y_train)
y_pred=lm.predict(x_test)
print(y_pred)


# In[18]:


a=lm.coef_
b=lm.intercept_
print("estimated model slope,a:",a)
print("estimated model intercept,b",b)


# In[20]:


from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,y_pred)
rmse=np.sqrt(mse)
print("RMSE value: {:.4f}".format(rmse))


# In[25]:


from sklearn.metrics import r2_score
print("r2 score value:{:.4f}".format(r2_score(y_test,y_pred)))


# In[28]:


plt.scatter(x,y, color='blue',label = "Scatter Plot")
plt.plot(x_test,y_pred,color="black",linewidth=3,label="regression line")
plt.title("Relationship between sales and advertising")
plt.xlabel("sales")
plt.ylabel("advertising")
plt.legend(loc=4)
plt.show()


# In[ ]:




