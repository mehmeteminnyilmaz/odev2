#Girilen metnin belirlenen s�n�rdan daha m� az yoksa daha m� fazla harfi oldu�unu kontrol edip ona g�re yeni uzunluk de�eri d�nd�ren fonksiyon
#E�er daha az veya e�itse 'length'e metnin uzunlu�u atan�yor
#E�er daha fazlaysa 'length'e belirlenen s�n�r (max_num) atan�yor
def text_length(text, max_num):
    if len(text) <= max_num:
        length = len(text)
    else:
        length = max_num
    return length

#Bir harfin girilen metindeki belirli aral�kta ka� tane oldu�unu d�nd�ren fonksiyon
def count_letter(length, text, letter):
    return text.count(letter, 0, length)

#Girilen metnin ilk y�z m�, bin mi yoksa on bin harfinde mi tek tek harflerin say�lar�n� ve bulunma oranlar�n� d�nd�ren fonksiyon
#1, 2 ve 3 rakamlar� �st s�n�r� belirliyor ve ona g�re yukar�daki fonksiyonlarda da gerekli arg�manlar belirleniyor
#En sonda da harflerin metindeki say�s�yla bulunma y�zdeleri geri d�nd�r�l�yor 
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

#Benim temel okul bilgilerimi ekrana yazd�ran fonksiyon
#��inde 'student' s�zl��� bulunmakta
#�stenilen herhangi bir 'key' se�ilerek kar��s�ndaki bilgi ekrana yazd�r�l�r
def student_info(std_info):
    print(std_info)
    
student = {
    "name": "Mehmet Emin",
    "last name": "Yilmaz",
    "number": "211213036",
    "message": "Congratulations!"
    }
