#1)------------------------------------------------------------------
acilar = [int(input("Birinci değer :")), int(input("İkinci değer :")), int(input("Üçüncü değer :"))]
toplam = sum(acilar)

if toplam >= 180:
    print("Üçgeniniz Geniş Açılı Bir Üçgendir")
elif toplam == 90:
    print("Üçğeniniz Dik Açılıdır")
else:
    print("Üçgeniniz Dar Açılıdır")

#2)--------------------------------------------------------------------

uzayli_rengi = str(input("Uzaylı Rengi Giriniz (kırmızı, yeşil, sarı)  :"))

if uzayli_rengi == "yeşil":
    print("Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız")
else:
    print("Tebrikler, yeşil olmayan uzaylıya ateş ettiğiniz için 10 puan ka zandınız ")

#3)----------------------------------------------------------------------

if uzayli_rengi == "yeşil":
    print("Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız")
elif uzayli_rengi == "sarı":
    print("Tebrikler, sarı uzaylıya ateş ettiğiniz için 10 puan kazandınız")
elif uzayli_rengi == "kırmızı":
    print("Tebrikler, kırmızı uzaylıya ateş ettiğiniz için 15 puan kazandınız")
else:
    print("Hiçbir uzaylıyı tutturamadınız :(")

#4)-----------------------------------------------------------------------

yas = int(input("Yaşınızı Girin :"))

if yas <2 :
    print("Bu insan bebektir.")
elif 2 <= yas <= 4:
    print("Bu insan yeni yürümeye başlayan çocuktur")
elif 4 <= yas <= 13:
    print("Bu insan çocuktur")
elif 13 <= yas <= 20:
    print("Bu insan ergendir")
elif 20 <= yas <= 65:
    print("Bu insan yetişkindir")
else:
    print("Bu insan yaşlıdır")

#5)---------------------------------------------------------------------

favori_meyveler =["ayva", "çekirdeksiz sarı üzüm", "incir", "kiraz", "nektari"]
ornek_meyveler =["elma", "armut", "karpuz", "kavun", "muz", "portakal", "çilek", "vişne", "kiraz", "mandalina"]

for i in range(len(favori_meyveler)):
    olmayan_meyveler =[]
    if favori_meyveler[i] != ornek_meyveler[i]:
        olmayan_meyveler = [ornek_meyveler[i]]
        print("Listenizde olmayan meyveler : " + ', '.join(olmayan_meyveler))

