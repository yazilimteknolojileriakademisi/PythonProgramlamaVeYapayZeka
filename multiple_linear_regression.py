#!/usr/bin/env python
# coding: utf-8

# # MULTIPLE LINEAR REGRESSION
# 
# Multiple Linear Regression'da birden fazla bağımsız(independent) değişkene karşılık bir bağımlı(dependent) dğeişken bulunur.
# 
# Linear Regression veriler arasında var olan korelasyonu(ilişkiyi) kullanarak yeni gelecek verileri tahmin etme modelidir. Burada makine öğrenimi bize veriler arasındaki bu ilişkiyi belirlememize yardımcı olur ve bu sayede yeni verileri tahmin edebiliriz. 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
# sklearn library
from sklearn import linear_model

# veri setimizi import ediyoruz, ayraç olarak noktalı virgül olduğu için bunu belirtiyoruz:
df = pd.read_csv("multilinearregression.csv",sep = ";")



# In[2]:


# Veri setimizi görelim ve doğru import ettiğiniz kontrol edelim:
df


# In[3]:


df[['alan', 'odasayisi', 'binayasi']]


# In[4]:


df['fiyat']


# In[5]:


# linear regression modeli tanımlıyoruz:

reg = linear_model.LinearRegression()
reg.fit(df[['alan', 'odasayisi', 'binayasi']], df['fiyat'])

# Prediction yapalım..

reg.predict([[230,4,10]])


# In[10]:


reg.predict([[230,6,0]])


# In[11]:


reg.predict([[355,3,20]])


# In[12]:


reg.predict([[230,4,10], [230,6,0], [355,3,20]])


# In[13]:


reg.coef_


# In[14]:


reg.intercept_


# In[15]:


# Multiple Linear regression formülümüze dönersek hatırlayalım:
# y= a + b1X1 + b2X2 + b3X3 + ... formülümüzdü

a = reg.intercept_
b1 = reg.coef_[0]
b2 = reg.coef_[1]
b3 = reg.coef_[2]

x1 = 230
x2 = 4
x3 = 10
y = a + b1*x1 + b2*x2 + b3*x3

y


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




