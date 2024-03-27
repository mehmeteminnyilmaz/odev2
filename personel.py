class Personel:
    def __init__(self, ad, dep, yil, maas):
        self.ad = ad
        self.dep = dep
        self.yil = yil
        self.maas = maas

class Firma():
    personel_listesi = []
    
    def personel_ekle(self, kisi):
        self.personel_listesi.append(kisi)
    
    def personel_listele(self):
        for i in range(len(self.personel_listesi)):
            print(self.personel_listesi[i].ad, self.personel_listesi[i].dep, self.personel_listesi[i].yil, self.personel_listesi[i].maas)

    def maas_zammi(self, kisi, zam_orani):
        kisi.maas = kisi.maas * (100 + zam_orani) // 100
     
    def personel_cikart(self, kisi):
        self.personel_listesi.remove(kisi)
