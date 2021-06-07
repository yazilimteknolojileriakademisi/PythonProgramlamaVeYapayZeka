# .......................................
#.                                      .
#.          DÖNGÜLER - while loop       .
#.                                      .
# .......................................

"""
    Döngüler, kod bloğu içerisindeki kodları verilen şart sağlandığı sürece tekrar tekrar 
 çalışmasını sağlayan yapılardır. Bir işi birden fazla yapacağımız durumlarda kullanırız. Kolaylığı ve sürekliliği sağlarlar.
 Döngünün durması için verilen şartın yanlış hale gelmesi gerekir. Python’ da iki tane döngü vardır:
 while, for.
 
 şimdi while döngüsünü inceleyelim.

"""


"""
while <şart>:
    <burada yazılan işlemleri yap>
"""

# Kendisine gönderilen sayının faktöryelini hespalayıp return eden bir fonksiyon yazınız..

# Örneğin sayi = 4 olsun,  4'ün faktröyeli= 4*3*2*1 = 24
"""
def faktoryel_hesapla(sayi):
    sonuc = 1;
    while (sayi>0):
        sonuc = sonuc * sayi
        sayi = sayi - 1
    return sonuc

x = int(input("Lütfen faktöryeli hesaplanacak sayiyi giriniz: "))
print(faktoryel_hesapla(x))
"""

# Quiz:
# echo programı: Kullanıcı ne yazarsa aynısını ekrana yazan bir program yapınız. 
# program sürekli çalışsın ancak kullanıcı kapat yazarsa program kapansın.

# Çözüm:

mesaj = input("Bir şeyler yaz:")
while (mesaj != "kapat"):
    print(mesaj)
    mesaj = input("Bir şeyler yaz:")
    

    





