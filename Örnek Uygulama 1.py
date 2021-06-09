# .........................
# . Uygulama              .
# . Hesap Makinesi        .
# .                       .
# .........................

"""
Gereksinimler:

1.Program kullanıcıdan önce bir sayı girmesini istecektir
2.Program kullanıcıya 4 işlem menüsünü seçenekli olarak sunacak ve kullanıcının bir aritmetik işlem seçmesini isteyecektir.
3.Program kullanıcıdan ikinci bir sayı girmesini isteyecektir.
4.Program kullanıcıya yapılan işlemi ve sonucunu ekrana yazarak gösterecektir.

"""

# 1.aşama
sayi1 = int(input("Lütfen İlk sayıyı giriniz"))

# 2. aşama
print("İşlemler:")
print("1 Toplama")
print("2 Çıkarma")
print("3 Çarpma")
print("4 Bölme")
islem = int(input("Lütfen 1 ile 4 arasında bir işlem seçiniz"))

# 3. aşama
sayi2 = int(input("Lütfen İkinci sayıyı giriniz"))

#4. aşama
def hesapla(deger1, deger2, islem):
    if (islem == 1):
        return deger1 + deger2
    elif (islem == 2):
        return deger1 - deger2
    elif (islem ==3):
        return (deger1 * deger2)
    elif (islem == 4):
        return deger1 / deger2


if (islem >= 1) and (islem <= 4):
    sonuc = hesapla(sayi1, sayi2, islem)
    print(sayi1, " ile ", sayi2, " islem no: ", islem, " Sonucu: ", sonuc)
else:
    print("Girdiğiniz islem numarasi 1-4 arasında olmalıdır..")


    



