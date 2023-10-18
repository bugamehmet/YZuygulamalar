#1)-----------------------------------------------------------

deger = int(input("bir değer girin : "))
if deger == 0:
    print("Sıfırla çarpılan her sayı sıfırdır.")
else:
    for i in range(10):
        deger1=deger*(i+1)
        print(deger1)

#2)--------------------------------------------------------------

deger_basamak = int(input("bir değer girin : "))
i = 0
while i < deger_basamak:
    deger_basamak = deger_basamak/10
    i+=1
print('Sayınız ' + str(i) + ' Basamaklıdır.')

#3)----------------------------------------------------------------

#for ile :
sayisalDegerler = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
besebolunen =[]
for i in sayisalDegerler:
    if i % 5 == 0:
        besebolunen.append(i)
        if i >= 150:
            break
print("Bese bölünen sayilar : " + str(besebolunen))

#while ile :

sayisalDegerler2 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
besebolunen2 =[]
i = 0
while i< len(sayisalDegerler2):
    if sayisalDegerler2[i] % 5 == 0:
        besebolunen2.append(sayisalDegerler2[i])
        if sayisalDegerler2[i] >=150:
            break
    i+=1
print("Bese bölünen sayilar2 : " + str(besebolunen2))

#4)----------------------------------------------------------------

degerler = [int(input("a değeri : ")), int(input("b değeri : ")), int(input("c değeri : "))]

if degerler[0] > degerler[1]:
    count_büyük = degerler[0]
    count_kücük = degerler[1]
else:
    count_büyük = degerler[1]
    count_kücük = degerler[0]

sayac = 0
while count_büyük >= count_kücük:
    if count_kücük % degerler[2] == 0:
        sayac+=1
    count_kücük+=1
print(f"{degerler[0]} ve {degerler[1]} sayilari arasında kaç sayının {degerler[2]}'ye bölündüğü : {sayac}")

#5)-------------------------------------------------------------------

for i in range(1,10):
    #print(str(i) + " - " + str(10-i))
    print(f"{i} - {10 - i}")

#6)-------------------------------------------------------------------

ip = str(input("IP adresinizi giriniz : "))

bolunmus = [int(i) for i in ip.split(" ")]
for i in range(5):
    bolunmus[3] += 1
    if bolunmus[3] > 255:
        bolunmus[3] = 0
        bolunmus[2] += 1
        if bolunmus[2] > 255:
            bolunmus[2] = 0
            bolunmus[1] += 1
            if bolunmus[1] > 255:
                bolunmus[1] = 0
                bolunmus[0] += 1
    print(f"{bolunmus[0]} {bolunmus[1]} {bolunmus[2]} {bolunmus[3]}")