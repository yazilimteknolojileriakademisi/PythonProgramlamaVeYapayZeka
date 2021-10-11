# -*- coding: utf-8 -*-
"""
 PYTHON PROGRAMLAMA UYGULAMASI/QUIZ:
 
 Bir tamsayı listesi içindeki çift sayıları bulan bir fonksiyon yazınız..
 Örnek:
     liste = [ 1, 5, 7, 8, 12, 45, 78, 121 ]
   ise
     Cevabınız: 3 olmalı...
"""

def cift_sayilari_bul(sayilar):
    sayac = 0
    for sayi in sayilar:
        if (sayi % 2 == 0):            
            sayac += 1
    return sayac

    
liste = [ 1, 5, 7, 8, 12, 45, 78, 121, 2, 4 ]
print(cift_sayilari_bul(liste))
