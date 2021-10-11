# -*- coding: utf-8 -*-
"""
 PYTHON PROGRAMLAMA UYGULAMA ÇALIŞMASI/QUIZ:
 
 Bir tamsayının Faktöryelini recursion(*) kullanarak hesaplayan bir fonksiyon yazınız..
 Örnek:
     Sayi = 5
   ise
     Cevabınız: 120 (5*4*3*2*1) olmalı...
     
* Bilgi:
  Kendi kendini çağıran fonksiyonlara recursive fonksiyon denilir.
"""


def hesapla(n):
    if (n == 1 or n==0):
        return 1
    else:
        return (n * hesapla(n-1))


print(hesapla(5))

