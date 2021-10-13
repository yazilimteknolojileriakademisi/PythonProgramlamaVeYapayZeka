# -*- coding: utf-8 -*-
"""
 PYTHON PROGRAMLAMA UYGULAMA ÇALIŞMASI/QUIZ:
 
 Bir sayının asal olup olmadığını hesaplayan bir fonksiyon yazınız.
 Örnek:
    2: Asal
    3: Asal
    4: Asal değil.
    
    1 ile 100 arasındaki asal sayılar: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 ve 97.
     
* Bilgi:
  Asal Sayı Nedir? Asal sayılar yalnız kendisi ile bölünebilen tüm doğal sayılardır.
  1 asal sayı olarak kabul edilmez.
"""

def asal_bul(sayi):  
    asalsayi_mi = True
    if (sayi > 1):
        for i in range(2,sayi):
            if (sayi % i) == 0:
                asalsayi_mi = False
                break
    if (asalsayi_mi == True):
        print(sayi, "  Asal sayıdır")
    else:
        print(sayi, "  Asal sayı değildir!")

for x in range(2,101):
    asal_bul(x)


