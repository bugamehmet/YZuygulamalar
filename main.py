import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# https://mmo.org.tr/sites/default/files/deb1c54814305ca_ek.pdf

bulasikMiktari = ctrl.Antecedent(np.arange(0, 101, 15), "Bulaşık Miktarı")
kirlilikDerecesi = ctrl.Antecedent(np.arange(0, 101, 15), "Kirlilik Derecesi")
bulasikCinsi = ctrl.Antecedent(np.arange(0, 101, 15), "Bulaşık Cinsi")

yikamaZamani = ctrl.Consequent(np.arange(30, 161, 10), "Yıkama Zamanı")
deterjanMiktari = ctrl.Consequent(np.arange(0, 93, 17.5), "Deterjan Miktarı")
suSicakligi = ctrl.Consequent(np.arange(35, 68, 2.5), "Su Sıcaklığı")
üstpompaDevri = ctrl.Consequent(np.arange(2100, 3501, 100), "Üst Sepet Pompa Devri")
altpompaDevri = ctrl.Consequent(np.arange(2100, 3501, 100), "Alt Sepet Pompa Devri")

bulasikMiktari["AZ"] = fuzz.trimf(bulasikMiktari.universe, [-35, 0, 35])
bulasikMiktari["ORTA"] = fuzz.trimf(bulasikMiktari.universe, [15, 40, 85])
bulasikMiktari["ÇOK"] = fuzz.trimf(bulasikMiktari.universe, [65, 100, 135])

kirlilikDerecesi["AZ KİRLİ"] = fuzz.trimf(kirlilikDerecesi.universe, [-35, 0, 35])
kirlilikDerecesi["ORTA KİRLİ"] = fuzz.trimf(kirlilikDerecesi.universe, [15, 40, 85])
kirlilikDerecesi["ÇOK KİRLİ"] = fuzz.trimf(kirlilikDerecesi.universe, [65, 100, 135])

bulasikCinsi["HASSAS"] = fuzz.trimf(bulasikCinsi.universe, [-35, 0, 35])
bulasikCinsi["KARMA"] = fuzz.trimf(bulasikCinsi.universe, [15, 40, 85])
bulasikCinsi["GÜÇLÜ"] = fuzz.trimf(bulasikCinsi.universe, [65, 100, 135])

yikamaZamani["ÇOK KISA"] = fuzz.trimf(yikamaZamani.universe, [-60, 1, 60])
yikamaZamani["KISA"] = fuzz.trimf(yikamaZamani.universe, [40, 75, 90])
yikamaZamani["ORTA"] = fuzz.trimf(yikamaZamani.universe, [70, 95, 120])
yikamaZamani["UZUN"] = fuzz.trimf(yikamaZamani.universe, [100, 125, 150])
yikamaZamani["ÇOK UZUN"] = fuzz.trimf(yikamaZamani.universe, [130, 155, 180])

deterjanMiktari["ÇOK AZ"] = fuzz.trimf(deterjanMiktari.universe, [-17.5, 0, 17.5])
deterjanMiktari["AZ"] = fuzz.trimf(deterjanMiktari.universe, [7.5, 25, 42.5])
deterjanMiktari["NORMAL"] = fuzz.trimf(deterjanMiktari.universe, [32.5, 50, 67.5])
deterjanMiktari["ÇOK"] = fuzz.trimf(deterjanMiktari.universe, [57.5, 75, 92.5])
deterjanMiktari["ÇOK FAZLA"] = fuzz.trimf(deterjanMiktari.universe, [82.5, 100, 117.5])

suSicakligi["DÜŞÜK"] = fuzz.trimf(suSicakligi.universe, [-20, 0, 50])
suSicakligi["NORMAL"] = fuzz.trimf(suSicakligi.universe, [37.5, 52.5, 67.5])
suSicakligi["YÜKSEK"] = fuzz.trimf(suSicakligi.universe, [55, 70, 80])

üstpompaDevri["ÇOK DÜŞÜK"] = fuzz.trimf(üstpompaDevri.universe, [2000, 2200, 2400])
üstpompaDevri["DÜŞÜK"] = fuzz.trimf(üstpompaDevri.universe, [2300, 2500, 2700])
üstpompaDevri["ORTA"] = fuzz.trimf(üstpompaDevri.universe, [2600, 2800, 3000])
üstpompaDevri["YÜKSEK"] = fuzz.trimf(üstpompaDevri.universe, [2900, 3100, 3300])
üstpompaDevri["ÇOK YÜKSEK"] = fuzz.trimf(üstpompaDevri.universe, [3200, 3400, 3600])

altpompaDevri["ÇOK DÜŞÜK"] = fuzz.trimf(altpompaDevri.universe, [2000, 2200, 2400])
altpompaDevri["DÜŞÜK"] = fuzz.trimf(altpompaDevri.universe, [2300, 2500, 2700])
altpompaDevri["ORTA"] = fuzz.trimf(altpompaDevri.universe, [2600, 2800, 3000])
altpompaDevri["YÜKSEK"] = fuzz.trimf(altpompaDevri.universe, [2900, 3100, 3300])
altpompaDevri["ÇOK YÜKSEK"] = fuzz.trimf(altpompaDevri.universe, [3200, 3400, 3600])

kural1 = ctrl.Rule(bulasikMiktari["AZ"] & kirlilikDerecesi["AZ KİRLİ"] & bulasikCinsi["HASSAS"], yikamaZamani["ÇOK KISA"])
kural2 = ctrl.Rule(bulasikMiktari["AZ"] & kirlilikDerecesi["AZ KİRLİ"] & bulasikCinsi["HASSAS"], deterjanMiktari["ÇOK AZ"])
kural3 = ctrl.Rule(bulasikMiktari["AZ"] & kirlilikDerecesi["AZ KİRLİ"] & bulasikCinsi["HASSAS"], suSicakligi["DÜŞÜK"])
kural4 = ctrl.Rule(bulasikMiktari["AZ"] & kirlilikDerecesi["AZ KİRLİ"] & bulasikCinsi["HASSAS"], üstpompaDevri["DÜŞÜK"])
kural5 = ctrl.Rule(bulasikMiktari["AZ"] & kirlilikDerecesi["AZ KİRLİ"] & bulasikCinsi["HASSAS"], altpompaDevri["DÜŞÜK"])

kural6 = ctrl.Rule(bulasikMiktari["AZ"] & kirlilikDerecesi["ÇOK KİRLİ"] & bulasikCinsi["KARMA"], yikamaZamani["ORTA"])
kural7 = ctrl.Rule(bulasikMiktari["AZ"] & kirlilikDerecesi["ÇOK KİRLİ"] & bulasikCinsi["KARMA"], deterjanMiktari["NORMAL"])
kural8 = ctrl.Rule(bulasikMiktari["AZ"] & kirlilikDerecesi["ÇOK KİRLİ"] & bulasikCinsi["KARMA"], suSicakligi["YÜKSEK"])
kural9 = ctrl.Rule(bulasikMiktari["AZ"] & kirlilikDerecesi["ÇOK KİRLİ"] & bulasikCinsi["KARMA"], üstpompaDevri["DÜŞÜK"])
kural10 = ctrl.Rule(bulasikMiktari["AZ"] & kirlilikDerecesi["ÇOK KİRLİ"] & bulasikCinsi["KARMA"], altpompaDevri["YÜKSEK"])


kural11 = ctrl.Rule(bulasikMiktari["ORTA"] & kirlilikDerecesi["ORTA KİRLİ"] & bulasikCinsi["GÜÇLÜ"], yikamaZamani["ORTA"])
kural12 = ctrl.Rule(bulasikMiktari["ORTA"] & kirlilikDerecesi["ORTA KİRLİ"] & bulasikCinsi["GÜÇLÜ"], deterjanMiktari["NORMAL"])
kural13 = ctrl.Rule(bulasikMiktari["ORTA"] & kirlilikDerecesi["ORTA KİRLİ"] & bulasikCinsi["GÜÇLÜ"], suSicakligi["NORMAL"])
kural14 = ctrl.Rule(bulasikMiktari["ORTA"] & kirlilikDerecesi["ORTA KİRLİ"] & bulasikCinsi["GÜÇLÜ"], üstpompaDevri["YÜKSEK"])
kural15 = ctrl.Rule(bulasikMiktari["ORTA"] & kirlilikDerecesi["ORTA KİRLİ"] & bulasikCinsi["GÜÇLÜ"], altpompaDevri["YÜKSEK"])

kural16 = ctrl.Rule(bulasikMiktari["ÇOK"] & kirlilikDerecesi["ÇOK KİRLİ"] & bulasikCinsi["KARMA"], yikamaZamani["ÇOK UZUN"])
kural17 = ctrl.Rule(bulasikMiktari["ÇOK"] & kirlilikDerecesi["ÇOK KİRLİ"] & bulasikCinsi["KARMA"], deterjanMiktari["ÇOK FAZLA"])
kural18 = ctrl.Rule(bulasikMiktari["ÇOK"] & kirlilikDerecesi["ÇOK KİRLİ"] & bulasikCinsi["KARMA"], suSicakligi["YÜKSEK"])
kural19 = ctrl.Rule(bulasikMiktari["ÇOK"] & kirlilikDerecesi["ÇOK KİRLİ"] & bulasikCinsi["KARMA"], üstpompaDevri["DÜŞÜK"])
kural20 = ctrl.Rule(bulasikMiktari["ÇOK"] & kirlilikDerecesi["ÇOK KİRLİ"] & bulasikCinsi["KARMA"], altpompaDevri["YÜKSEK"])

yikamaZamani_ctrl = ctrl.ControlSystem([kural1, kural2, kural3, kural4, kural5, kural6, kural7, kural8, kural9, kural10, kural11, kural12, kural13, kural14, kural15, kural16, kural17, kural18, kural19, kural20])
yikamaZamani_sim = ctrl.ControlSystemSimulation(yikamaZamani_ctrl)
yikamaZamani_sim.input['Bulaşık Miktarı'] = 62
yikamaZamani_sim.input['Kirlilik Derecesi'] = 40.1
yikamaZamani_sim.input['Bulaşık Cinsi'] = 88.7

yikamaZamani_sim.compute()

yikama_zamani = yikamaZamani_sim.output['Yıkama Zamanı']
deterjan_miktari = yikamaZamani_sim.output['Deterjan Miktarı']
su_sicakligi = yikamaZamani_sim.output['Su Sıcaklığı']
ust_pompa = yikamaZamani_sim.output['Üst Sepet Pompa Devri']
alt_pompa = yikamaZamani_sim.output['Alt Sepet Pompa Devri']

print(f"Yıkama Zamanı: {yikama_zamani}",
      f"Deterjan Miktarı: {deterjan_miktari}",
      f"Su Sıcaklığı: {su_sicakligi}",
      f"Üst Sepet Pompa Devri: {ust_pompa}",
      f"Alt Sepet Pompa Devri: {alt_pompa}", sep='\n')

