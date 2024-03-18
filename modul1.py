#Girilen metnin belirlenen sýnýrdan daha mý az yoksa daha mý fazla harfi olduðunu kontrol edip ona göre yeni uzunluk deðeri döndüren fonksiyon
#Eðer daha az veya eþitse 'length'e metnin uzunluðu atanýyor
#Eðer daha fazlaysa 'length'e belirlenen sýnýr (max_num) atanýyor
def text_length(text, max_num):
    if len(text) <= max_num:
        length = len(text)
    else:
        length = max_num
    return length

#Bir harfin girilen metindeki belirli aralýkta kaç tane olduðunu döndüren fonksiyon
def count_letter(length, text, letter):
    return text.count(letter, 0, length)

#Girilen metnin ilk yüz mü, bin mi yoksa on bin harfinde mi tek tek harflerin sayýlarýný ve bulunma oranlarýný döndüren fonksiyon
#1, 2 ve 3 rakamlarý üst sýnýrý belirliyor ve ona göre yukarýdaki fonksiyonlarda da gerekli argümanlar belirleniyor
#En sonda da harflerin metindeki sayýsýyla bulunma yüzdeleri geri döndürülüyor 
def max_letter(text, num, letter):
    if num == 1:
        t = text_length(text, 100)
        c = count_letter(t, text, letter)
    elif num == 2:
        t = text_length(text, 1000)
        c = count_letter(t, text, letter)
    elif num == 3:
        t = text_length(text, 10000)
        c = count_letter(t, text, letter)
    rate = c / t * 100
    return c, rate

#Benim temel okul bilgilerimi ekrana yazdýran fonksiyon
#Ýçinde 'student' sözlüðü bulunmakta
#Ýstenilen herhangi bir 'key' seçilerek karþýsýndaki bilgi ekrana yazdýrýlýr
def student_info(std_info):
    print(std_info)
    
student = {
    "name": "Mehmet Emin",
    "last name": "Yilmaz",
    "number": "211213036",
    "message": "Congratulations!"
    }
