# .......................................
#.                                      .
#.       Python'da Object Oriented      .
#.              Programlama 2           .
# .......................................


class Kara_Araci():
    hiz = 0
    def __init__(self, beygir_gucu, teker_sayisi):
        self.beygir_gucu = beygir_gucu
        self.teker_sayisi = teker_sayisi

    def hizi_ayarla(self, deger):
        self.hiz = deger



class Otobus(Kara_Araci):
    def __init__(self, beygir_gucu, teker_sayisi, yolcu_kapsasitesi):
        Kara_Araci.__init__(self, beygir_gucu, teker_sayisi)
        self.yolcu_kapsasitesi= yolcu_kapsasitesi
    def takograf_kontrol(self):
        print("Takograf kontrol edildi")


class Otomobil(Kara_Araci):
    def __init__(self, beygir_gucu, teker_sayisi, sunroof):
        Kara_Araci.__init__(self, beygir_gucu, teker_sayisi)
        self.sunroof = sunroof




otomobil1 = Otomobil(120, 4, "Var")
otomobil1.hizi_ayarla(70)


otobus1 = Otobus(450, 8, 44)
otobus1.hizi_ayarla(80)

print(otobus1.beygir_gucu, "  ", otobus1.hiz)


otobus1.takograf_kontrol()

