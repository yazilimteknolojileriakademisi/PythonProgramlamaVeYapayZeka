# .......................................
#.                                      .
#.       Dosyalar ile Çalışmak          .
#.  Metin Dosyası Açma / Yazma / Okuma  .
# .......................................

import os



# ogrenciler.txt dosyasında bulunan metni okuyacağız
ogrenci_dosya = os.open("ogrenciler.txt", os.O_RDONLY)
dosya_uzunluk = os.stat(ogrenci_dosya).st_size
icerik = os.read(ogrenci_dosya, dosya_uzunluk)

ogrenciler = icerik.decode()


ogrenciler_list = ogrenciler.split("\n")

#print(ogrenciler_list)
ogrenci_sayisi = len(ogrenciler_list)-1
#print(ogrenci_sayisi)

index = 0
toplam_notlar = 0
while (index < ogrenci_sayisi):
    #print(ogrenciler_list[index])
    ogrenci_notu = ogrenciler_list[index].split(",")
    toplam_notlar = toplam_notlar + int(ogrenci_notu[1])
    index = index + 1


print("Ogrencilerin sınav notlarının ortalaması : ", toplam_notlar/ogrenci_sayisi)

os.close(ogrenci_dosya)





