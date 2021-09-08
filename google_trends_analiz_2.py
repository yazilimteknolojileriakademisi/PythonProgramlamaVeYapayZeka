# -*- coding: utf-8 -*-
# .......................................
#.                                      .
#.           GOOGLE TRENDS ANALİZİ - 2  .
#.                                      .
#........................................

import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq

pytrends = TrendReq()

# payload build işlemini yaparken keyword listemizi oluşturalım. Bu kez sadece Python kelimesi
# ile ilgili analizler yapacağız...
pytrends.build_payload(kw_list=['python'], timeframe='2015-01-01 2021-09-01', geo='TR') 

# related topics'leri bulalım...
df_rt = pytrends.related_topics()

lst = df_rt['python']

# rising popularity topics :


# Rising ile ilgili Dataframe bize  Python ile ilgili olarak yükselen arama trendini gösterir
rising_values = df_rt['python']['rising']
#print(rising_values.head())



# related queries ile de Python ile alakalı Google search kelimelerini bulur..
# Bunların içinde 2 tane Dataframe bulunur, birisi top diğeri rising isimli Dataframe'lerdir..
df_rq = pytrends.related_queries()
#print(df_rq['python']['rising'].head())
print(df_rq['python']['top'].head())

#--------------------------------------------------

# Son olarak da belirli bir yıl içinde toplamda en fazla hit alan arama kelimelerini getirtelim...
#print(pytrends.top_charts(date='2020', geo='US'))


