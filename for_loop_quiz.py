# .......................................
#.                                      .
#.             DÖNGÜLER - for loop      .
#.                                      .
# .......................................

"""
    Döngüler, kod bloğu içerisindeki kodları verilen şart sağlandığı sürece tekrar tekrar 
 çalışmasını sağlayan yapılardır. Bir işi birden fazla yapacağımız durumlarda kullanırız. Kolaylığı ve sürekliliği sağlarlar.
 Döngünün durması için verilen şartın yanlış hale gelmesi gerekir. Python’ da iki tane döngü vardır:
 while, for. for döngüsü ile başlıyoruz.

"""

ogrenci_list = [ "Ahmet Emre", "Ali Öz", "Veli Can", "Ayşe Su", "Batuhan Emre"]


# Quiz:
# Kullanicidan bir isim isteyin. Bu ismin öğrencli listesinde olup olmadığını bulun ve kullanıcıya mesaj verin.

# Çözüm:

aranan_isim = input("Lütfen ad soyad giriniz: ")

ogrenci_listede_mevcut = False

for ogrenci in ogrenci_list:
    if (ogrenci == aranan_isim):
        ogrenci_listede_mevcut = True

if (ogrenci_listede_mevcut == True):
    print("Öğrenci sınıfımızda mevcuttur!")
else:
    print("Öğrenci msınıfmızda kayıtlı değildir")






    
