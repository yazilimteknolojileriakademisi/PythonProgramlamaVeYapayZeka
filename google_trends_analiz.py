# -*- coding: utf-8 -*-
# .......................................
#.                                      .
#.           GOOGLE TRENDS ANALİZİ - 1  .
#.                                      .
#........................................

import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq


pytrends = TrendReq()


# keywords listimizi oluşturalım..
kw_list = ["python", "java", "javascript", "visual basic"] 


# payload build işlemini yapıyoruz...
pytrends.build_payload(kw_list, cat=None, timeframe='2010-01-01 2021-09-01', geo='US') 

# zamana göre dağılımı isteyelim...
df = pytrends.interest_over_time()

# Dataframe'imizi excel dosyası olarak kaydedelim..
df.to_excel("us_prog_lang_trends.xls")


# tarihe göre çizim yaptıralım...
plt.figure(figsize=(10, 8))
plt.plot(df.index,df.python,'k*')
plt.plot(df.index,df.java,'r*')
plt.plot(df.index,df.javascript,'b*')
plt.plot(df.index,df["visual basic"],'g*')
plt.legend(['python','java','javascript', "visual basic"])

plt.show()


# Detaylı bilgi ve diğer metodlar için lütfen aşağıdaki URL'i ziyaret ediniz:
# https://pypi.org/project/pytrends/
