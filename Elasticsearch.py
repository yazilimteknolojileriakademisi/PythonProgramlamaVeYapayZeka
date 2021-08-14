#!/usr/bin/env python
# coding: utf-8

# # &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ELASTIC SEARCH 
# <IMG src="./elasticsearch-logo.png" width="100" height="100" >
#     
# Index — Database
# 
# Datatype — Type of the document
# 
# Id — Id of the document
#     
# Elasticsearch kütüphanesini kullanmadan önce aşağıdaki komutla Anaconda Python sistemimize elasticsearch modülünü eklememiz gerekiyor, bu amaçla MSDOS komut satırından aşağıdaki komutu çalıştırın:
# 
# conda install elasticsearch 
# 

# In[1]:


# Import Elasticsearch package 
from elasticsearch import Elasticsearch 

# elastic clusterına bağlanalım..
es=Elasticsearch([{'host':'localhost','port':9200}])
es


# In[2]:


# Employee yani çalışan bilgilerini elasticsearch sistemimize ekleyeceğiz..
e1={
    "first_name":"Nihat",
    "last_name":"Pancar",
    "age": 27,
    "about": "Love to play cricket",
    "interests": ['sports','music'],
}
print(e1)


# ### Inserting a document:

# In[3]:


# Şimdi bu dökümanı Elasticsearch içinde saklayalım..
res = es.index(index='sirketpersonelvt',id=1,body=e1)


# ##### Birkaç kişi daha ekleyelim:

# In[4]:


# 2 kişi daha ekleyelim..
e2={
    "first_name" :  "Can",
    "last_name" :   "Soykan",
    "age" :         32,
    "about" :       "I like to collect rock albums",
    "interests":  [ "music" ]
}
e3={
    "first_name" :  "Demir",
    "last_name" :   "Firat",
    "age" :         35,
    "about":        "I like to build cabinets",
    "interests":  [ "forestry" ]
}
res=es.index(index='sirketpersonelvt', id=2,body=e2)

res=es.index(index='sirketpersonelvt', id=3,body=e3)


# #### Bir Dökümanı Sistemden Sorgulama Yaparak Bulalım:

# In[5]:


res=es.get(index='sirketpersonelvt',id=3)
print(res)


# Esas döküman metni yani actual document ‘_source’ fieldinin içinde:

# In[6]:


print(res['_source'])


# #### Bir dökümanı silmek:

# In[7]:


res=es.delete(index='sirketpersonelvt', id=3)
print(res['result'])


# In[8]:


# sirketpersonelvt indexi içndeki tüm kayıtları sorgulayalım..
res= es.search(index='sirketpersonelvt',body={'query':{'match_all':{}}})
print(res)


# In[9]:


# Bu sonucun uzun hali, bunu kısaltmak için :
print(res['hits']['hits'])


# ### match operator:

# In[10]:


# İsmi Nihat olan dökümanları bulalım..
res= es.search(index='sirketpersonelvt',body={'query':{'match':{'first_name':'Nihat'}}})


# In[11]:


# Sonuca bakalım:
print(res)


# In[12]:


# Bu sonucun uzun hali, bunu kısaltmak için :
print(res['hits']['hits'])


# ### Full text search

# In[13]:


# Bir kayıt daha ekleyelim..
e4={
    "first_name":"Ali",
    "last_name":"Erkan",
    "age": 27,
    "about": "Love to play football",
    "interests": ['sports','music'],
}
res=es.index(index='sirketpersonelvt', id=4, body=e4)


# In[14]:


# Şimdi search yapalım:
res= es.search(index='sirketpersonelvt', body={
        'query':{
            'match':{
                "about":"play cricket"
            }
        }
    })
for hit in res['hits']['hits']:
    print(hit['_source']['about'])
    print(hit['_score'])
    print('**********************')


# ### Phrase Search
# 
# Phrase Search ile tüm kelimelerin birebir aynı olan eşlenikleri aranır..

# In[15]:


res= es.search(index='sirketpersonelvt', body={
        'query':{
            'match_phrase':{
                "about":"play cricket"
            }
        }
    })
for hit in res['hits']['hits']:
    print(hit['_source']['about']) 
    print(hit['_score'])
    print('**********************')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




