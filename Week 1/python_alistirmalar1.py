""" Q1: Verilen değerlerin veri yapılarını inceleyiniz."""

x = 8
type(x)

a = "hello"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

l = [1, 2, 3, 4, 5]
type(l)

d = {"a": "Jake",
     b: 2}
type(d)

t = ("a", "b", "c")
type(t)

s = {"a", "b", "c"}
type(s)


"""Q2: Verilen string ifadenin tum harflerini buyuk harfe ceviriniz. Virgül ve nokta yerine space koyunuz,
 kelime kelime ayırınız."""

text = "The goal is to turn data into information, and information into insight."
text = text.upper()
text = text.replace(",", " ")
text = text.replace(".", " ")
text = text.split()
print(text)


"""Q3: Verilen listeye aşağıdaki adımları uygulayınız.
#Adım 1: Verilen listenin eleman sayisina bakiniz.
 Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
 Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
 Adım 4: Sekizinci indeksteki elemanı siliniz.
 Adım 5: Yeni bir eleman ekleyiniz.
 Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz."""

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
print(len(lst))
print(lst[0], lst[10])
lst2 = lst[0:4]
lst[8] = ""
lst.append("S")
lst.insert(8, "N")
print(lst)


""" Q4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
 Adım 1: Key değerlerine erişiniz.
 Adım 2: Value'lara erişiniz.
 Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
 Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
 Adım 5: Antonio'yu dictionary'den siliniz."""

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}
print(dict.keys())
print(dict.values())
dict["Daisy"][1] = 13
dict["Ahmet"] = ["Turkey", 24]
dict.pop("Antonio")
print(dict)


""" Q5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu
 listeleri return eden fonksiyon yazınız."""
l = [2, 13, 18, 93, 22]


def func(l):
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd


""" Q6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır. 
  Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
   Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız."""

ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]
for i, j in enumerate(ogrenciler):
    if i < 3:
        print("Muhendislik Fakültesi", i + 1, ". öğrenci:", j)
    else:
        print("Tıp Fakültesi", i - 2, ". öğrenci:", j)


""" Q7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
 almaktadır. Zip kullanarak ders bilgilerini bastırınız."""

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]
for i in zip(ders_kodu, kredi, kontenjan):
    print("Kredisi", i[1], "olan", i[0], "kodlu dersin kontenjanı", i[2], "kişidir.")


""" Q8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
 eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir"""

kume1 = {"data", "python"}
kume2 = {"data", "function", "qcut", "lambda", "python", "miuul"}
if kume1.issuperset(kume2):
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))





