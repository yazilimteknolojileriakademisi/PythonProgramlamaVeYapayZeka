#!/usr/bin/env python
# coding: utf-8

# <H1>Pandas Modülü</H1>
# 
# Pandas genelde veri işleme ve temizlemede oldukça efektif şekilde kullanılan, ama esas olarak makine öğrenmesi gibi alanlarda oldukça fazla kullanılan bir python modülüdür.
# 
# Pandas modülü ağırlıklı olarak Dataframe adı verilen bir tür Tablo benzeri yapılar ile çalışır.
# 
# Dataframe'leri en iyi şekilde anlamak için örnekler üzerinden gideceğiz. Üzerinde çalışacağımız veri setini önce indirmekle işe başlıyoruz:
# 
# <H3>IMDB film veri setini indirme</H3>
# 
# Pandas örneklerimizde kullanacağımız IMDB film kitaplık dosyasını kursun başlangıcında indirdiğiniz materyaller isimli zipli dosyaiçeriğinden alıp eğitim sırasında oluşturduğumuz .py uzantılı python  dosyası ile aynı dizine koyuyoruz.
# 

# In[1]:


import pandas as pd


# pandas kütüphaneisni import ettikten sonra indirdiğimiz IMDB film veri setini df simini verdiğimiz bir DATAFRAME değişkeninin içine kopyalalım:

# In[3]:


df = pd.read_csv("imdb_top_1000.csv")


# Şimdi oluşturduğumuz datadrame'in ilk 5 satırını görüntüleyelim:

# In[4]:


df.head(5)


# Şimdi de son 5 satırını görelim:

# In[ ]:


df.tail(5)


# df.shape komutu ile dataframe'imizin boyutlarını görelim:

# In[ ]:


df.shape


# In[ ]:


len(df)


# Dataframe'deki Başlıklara bakalım:

# In[ ]:


df.columns


# Dataframe içindeki veri tiplerine bakalım:

# In[ ]:


df.dtypes


# df.isnull fonksiyonu ile verilerde eksik olan hücreleri görelim:

# In[ ]:


df.isnull()


# Tek bir sütuna bakalım:
#     

# In[ ]:


df["Series_Title"]


# 
# Tek bir sütunun ilk 5 kaydına bakalım:   

# In[ ]:


df["Series_Title"][:5]


# 
# Birden fazla sütunu bir değişkene atadığımızda o değişken de bir dataframe objesi olmaktadır:
#     

# In[ ]:


df2 = df[['Series_Title', 'Released_Year']]
df2


# <p>
# <p>
# <p>
# <p>
# Dataframe'i sıralama (sorting) etmek için sort_values kullanılır:

# In[ ]:


df.sort_values('Released_Year')


# 
# Yıllara göre film sayılarını bulmak için:
# 

# In[ ]:


df["Released_Year"].value_counts()


# 
# <H1> VERİ FİLTRELEME </H1>
# 

# Gelin Baba filminin IMDB rating'ini bulalım. 
# Eğer filmin datarframedeki sırasını biliyorsak basitçe dataframe'in IMBD_Rating sütununun 2.elemanını (ilk index 0 olduğu 
# için 1 diye yazıyoruz, listelerde ilk eleman 0'dan başlardı hatırlarsanız):

# In[ ]:


df['IMDB_Rating'][1]


# Ancak eğer Baba filminin veri setini görme şansımız yok yani büyük bir veri seti var içinde bir yerlerde o zaman kodla bulabiliriz:

# In[ ]:


df.loc[df['Series_Title']=="The Godfather"]["IMDB_Rating"]


# Bunu nasıl yaptığımızı anlatalım. Öncelikle 
# df.loc[df['Series_Title']=="The Godfather"] ile aslında Baba filminin olduğu satırı buluyoruz:

# In[ ]:


df.loc[df['Series_Title']=="The Godfather"]


# Ama bizim istediğimiz sadece IMDB_Rating değeri yani tüm satırı istemiyoruz, bu satırın içinden "IMDB_Rating" sütununu seçiyoruz
# 
# Bize df.loc ile dönen bir değişken var o değişken aslında bir dataframe bakınız:

# In[ ]:


type(df.loc[df['Series_Title']=="The Godfather"])


# O zaman bir dataframe'in basitçe sütununu seçmek için köşeli parantez kullanıyor ve seçiyoruz:

# In[ ]:


df.loc[df['Series_Title']=="The Godfather"]["IMDB_Rating"]


# Son olarak da IMDB_Rating değeri 8'in üstünde olan ve No_of_Votes 100000den çok olan filmleri görelim:

# In[ ]:


df.loc[(df['IMDB_Rating']>=8) & (df['No_of_Votes']>=100000)]


# Şimdi bir de IMDB_Rating değeri 8'in üstünde olan ve Gross değeri (yani gişe hasılatı) 30000000'dan çok olan filmleri görelim:

# In[ ]:


df.loc[(df['IMDB_Rating']>=8) & (df['Gross']>=30000000)]


# In[ ]:


#object tipinde olduğu için hata veriyor:
df.dtypes


# In[ ]:


# convert column "Gross" of a DataFrame
# to_numeric This function will try to change non-numeric 
# objects (such as strings) into integers or floating point numbers as appropriate.
df['Gross'] = df['Gross'].str.replace(",", "")
df["Gross"] = pd.to_numeric(df["Gross"])
type(df["Gross"][0])


# In[ ]:


df.loc[(df['IMDB_Rating']>=8.0) & (df['Gross']>=500000000)]


# 
# <H2> Manuel olarak Dataframe Oluşturma</H2>
# 
# Şimdiye kadar Dataframe'leri bir dosyadan oluşturup kullanmıştık. Şimdi de sıfırdan herhangi bir dosya kullanmadan ihtiyaç halinde kendimiz nasıl dataframe oluşturabiliriz onu öğreneceğiz.
# 
# random kütüphanesi kullanarak örnek bir array oluşturacağız.
# 

# In[ ]:


import random

randomlist1 = random.sample(range(15, 25), 2) 
randomlist2  = random.sample(range(15, 25), 2) 

randomlist1


# In[ ]:


randomlist2


# In[ ]:


randomlistoflists = [randomlist1, randomlist2]
randomlistoflists


# In[ ]:


columns = ["Sıcaklık 1.gün","Sıcaklık 2.gün"] 
mydataframe = pd.DataFrame(randomlistoflists,index = ["İst","Ankara"],columns = columns) 
mydataframe


# In[ ]:


type(mydataframe)


# In[ ]:


type(df)


# In[ ]:




