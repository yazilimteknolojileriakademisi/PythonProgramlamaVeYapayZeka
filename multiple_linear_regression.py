#!/usr/bin/env python
# coding: utf-8

# # MULTIPLE LINEAR REGRESSION
# 
# Multiple Linear Regression'da birden fazla bağımsız(independent) değişkene karşılık bir bağımlı(dependent) dğeişken bulunur.
# 
# Linear Regression veriler arasında var olan korelasyonu(ilişkiyi) kullanarak yeni gelecek verileri tahmin etme modelidir. Burada makine öğrenimi bize veriler arasındaki bu ilişkiyi belirlememize yardımcı olur ve bu sayede yeni verileri tahmin edebiliriz. 



import pandas as pd
import matplotlib.pyplot as plt
# sklearn library
from sklearn import linear_model

# veri setimizi import ediyoruz, ayraç olarak noktalı virgül olduğu için bunu belirtiyoruz:
df = pd.read_csv("multilinearregression.csv",sep = ";")

# Veri setimizi görelim ve doğru import ettiğiniz kontrol edelim:
df

df[['alan', 'odasayisi', 'binayasi']]

df['fiyat']


# linear regression modeli tanımlıyoruz:

reg = linear_model.LinearRegression()
reg.fit(df[['alan', 'odasayisi', 'binayasi']], df['fiyat'])

# Prediction yapalım..

reg.predict([[230,4,10]])


reg.predict([[230,6,0]])
reg.predict([[355,3,20]])
reg.predict([[230,4,10], [230,6,0], [355,3,20]])
reg.coef_
reg.intercept_


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


