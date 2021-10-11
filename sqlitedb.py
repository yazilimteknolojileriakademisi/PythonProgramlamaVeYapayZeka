#!/usr/bin/env python
# coding: utf-8

# # &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Python ile SQLite Veritabanı İşlemleri
# 
# 

# In[ ]:


# SQLite kullanabilmek için ilk olarak Python sqlite3 modülünü import etmemiz gerkeiyor..
import sqlite3
from sqlite3 import Error


# In[ ]:


# Daha sonra oluşturacağımız(veya daha önce zaten oluşturmuşsak bağlanacağımız) veritabanı için 
# bir connection nesnesi oluşturuan bir metod tanımlıyoruz..

def connection_olustur(db_file):    
    con = None
    try:
        con = sqlite3.connect(db_file)
        print("Connection oluşturuldu...")
    except Error as e:
        print("Hata oluştu : ", e)    
    return con         


# In[ ]:


# Yukarda tanımladığımız metodu kullanarak sqlite bağlantı nesnemizi oluşturuyoruz..
sqlite_connection = connection_olustur("kutuphane.db")


# In[ ]:


# Eğer herhangi bir hata nedeniyle veritabanı oluşturulamadıysa veya zaten varolan veritabanına
# bağlantı nesnesi oluşturulamadıysa bu durumda kullanıcıya bir hata mesajı verip 
# programdan çıkış yapmamız gerekir...
if (sqlite_connection == None):
    print("Veritabanına bağlantı sağlanılamadı, program kapanıyor..")
    exit()


# ### Veritabanında Tablo Oluşturma

# In[ ]:


# Tablo oluşturmak için önce bir cursor nesnesi oluşturmamız gerekiyor..
cursor = sqlite_connection.cursor()


# In[ ]:


# Tabloyu oluşturmak için (Tablo oluşturma sırasındaki hataları görüntüleyeceğimiz) bir
# fonksiyon yazalım..
def tablo_olustur(curs):        
    try:
        curs.execute("CREATE TABLE IF NOT EXISTS kitaplar (kitapadi TEXT, yazar TEXT, kitapno INT, sayfasayisi INT)")
    except Error as e:
        print("Hata oluştu : ", e)    


# In[ ]:


# kitaplar isimi tablomuzu kutuphane veritabanımız içinde oluşturalım..
tablo_olustur(cursor)
sqlite_connection.commit()


# ### Tabloya Kayıt Atma İşlemi

# In[ ]:


cursor.execute("INSERT INTO kitaplar VALUES ('Da Vinci Şifresi', 'Dan Brown', 1000, 495)")


# In[ ]:


sqlite_connection.commit()


# In[ ]:


cursor.execute("INSERT INTO kitaplar VALUES ('Dune', 'Frank Herbert', 1001, 296)")


# In[ ]:


sqlite_connection.commit()


# In[ ]:


cursor.execute("INSERT INTO kitaplar VALUES ('Yüzüklerin Efendisi', 'J.R.R. Tolkien', 1003, 1026)")


# In[ ]:


sqlite_connection.commit()


# ### Tablodan Veri Çekme

# In[ ]:


cursor.execute("SELECT * FROM kitaplar")


# In[ ]:


cekilen_veri = cursor.fetchall()


# In[ ]:


for each in cekilen_veri:
    print(each)


# In[ ]:





# In[ ]:


cursor.execute("SELECT * FROM kitaplar WHERE sayfasayisi > 400")


# In[ ]:


cekilen_veri = cursor.fetchall()


# In[ ]:


for each in cekilen_veri:
    print(each)


# In[ ]:





# In[ ]:


cursor.execute("SELECT * FROM kitaplar WHERE yazar = 'Dan Brown'")


# In[ ]:


cekilen_veri = cursor.fetchall()


# In[ ]:


for each in cekilen_veri:
    print(each)


# ### Tablodaki Verileri Güncelleme

# In[ ]:


cursor.execute("UPDATE kitaplar SET sayfasayisi = 999 WHERE sayfasayisi > 400")


# In[ ]:


cursor.execute("SELECT * FROM kitaplar")
cekilen_veri = cursor.fetchall()
for each in cekilen_veri:
    print(each)


# In[ ]:


sqlite_connection.commit()


# ### Tablodaki Verileri Silme

# In[ ]:


cursor.execute("DELETE FROM kitaplar WHERE kitapno = 1001")


# In[ ]:


sqlite_connection.commit()


# In[ ]:


cursor.execute("SELECT * FROM kitaplar")
cekilen_veri = cursor.fetchall()
for each in cekilen_veri:
    print(each)


# In[ ]:


# Son olarak da daha önce oluşturduğumuz veritabanı bağlantısını program bitişinde kapatıyoruz..
if sqlite_connection:
    sqlite_connection.close()


# In[ ]:





# In[ ]:





# In[ ]:




