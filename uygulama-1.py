import pandas as pd
import numpy as np

#a) --------------------------------------------------------------

csvdosyasi = pd.read_csv('uygulama-1111.csv', sep=';')

#b) ---------------------------------------------------------------

silinen = csvdosyasi.drop(columns=['Nem', 'Sıcaklık'])
print("Nem ve Sıcaklık değerleri silinmiş tablo :")
print(silinen)

#c) ------------------------------------------------------------------

veriler = {'Gün': ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14'],
        'Hava': ['Güneşli', 'Güneşli', 'Kapalı', 'Yağmurlu', 'Yağmurlu', 'Yağmurlu', 'Kapalı', 'Güneşli', 'Güneşli', 'Yağmurlu', 'Güneşli', 'Kapalı', 'Kapalı', 'Yağmurlu'],
        'Sıcaklık': ['Sıcak', 'Sıcak', 'Sıcak', 'Ilıman', 'Soğuk', 'Soğuk', 'Soğuk', 'Ilıman', 'Soğuk', 'Ilıman', 'Ilıman', 'Ilıman', 'Sıcak', 'Ilıman'],
        'Nem': ['Yüksek', 'Yüksek', 'Yüksek', 'Yüksek', 'Normal', 'Normal', 'Normal', 'Yüksek', 'Normal', 'Normal', 'Normal', 'Yüksek', 'Normal', 'Yüksek'],
        'Rüzgar': ['Seyrek', 'Aşırı', 'Seyrek', 'Seyrek', 'Seyrek', 'Aşırı', 'Aşırı', 'Seyrek', 'Seyrek', 'Seyrek', 'Aşırı', 'Aşırı', 'Seyrek', 'Aşırı'],
        'Oyun': ['Yok', 'Yok', 'Var', 'Var', 'Var', 'Yok', 'Var', 'Var', 'Yok', 'Var', 'Var', 'Yok', 'Var', 'Yok']}

tablo = pd.DataFrame(veriler)
bilgi = tablo.describe()
print("İstatiksel Bilgiler :")
print(bilgi)

#d) ----------------------------------------------------------------------

dizi1_d = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
dizi2_d = dizi1_d.reshape(6, 2)
print("(6,2) dizi : ")
print(dizi2_d)

#e) -------------------------------------------------------------------------

dizi1_e = np.random.rand(3, 3)
dizi2_e = np.random.rand(3, 3)

yataysiralama = np.hstack((dizi1_e, dizi2_e))
dikeysiralama = np.vstack((dizi1_e, dizi2_e))

print("Yatay Sıralama:")
print(yataysiralama)

print("Diley Sıralama:")
print(dikeysiralama)
