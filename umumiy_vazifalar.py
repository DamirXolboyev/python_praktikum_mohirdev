# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 06:52:37 2023

@author: xdamir
"""
# String mavzusiga oid vazifalar
# kocha = input("Ko'chani kiriting: ")
# mahalla = input("Mahallani kiriting: ")
# tuman = input("Tumanni kiriting: ")
# viloyat = input("Viloyatni kiriting: ")

# manzil = f"{kocha} ko\'chasi {mahalla} mahallasi {tuman} tumani {viloyat} viloyati\n"

# katta_harf = manzil.upper()

# kichkina_harf = manzil.lower()

# bosh_harf_katta = manzil.title()

# faqat_bosh_harf_katta = manzil.capitalize()

# print(manzil)

# print(katta_harf, kichkina_harf, bosh_harf_katta, faqat_bosh_harf_katta)

# print(f"{kocha} ko\'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati")

#Sonlar mavzusiga oid vazifalar

# son = int(input("Sonni kiriting: "))

# kvadrat = son ** 2

# kub = son ** 3

# print(f"{son} ning kvadrati {kvadrat} ga teng \n{son} ning kubi {kub} ga teng")

# yosh = int(input("Yoshingizni kiriting: "))

# t_yil = 2023 - yosh

# print(f"Siz {t_yil} da tug\'ilgansiz")

# son_1 = float(input("Birinchi sonni kiriting: "))

# son_2 = float(input("Ikkinchi sonni kiriting: "))

# qoshish = son_1 + son_2
# ayirish = son_1 - son_2
# kopaytirish = son_1 * son_2
# bolish = son_1 / son_2

# print(f"{son_1} + {son_2} = {qoshish}\n {son_1} - {son_2} = {ayirish}\n {son_1} * {son_2} = {kopaytirish}\n {son_1} + {son_2} = {bolish}\n")

#son = int(input("Istalgan butun son kiriting: "))

#for n in range(2,11):
#    if not (son%n):
#        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

"""

Xatolar bilan ishlash 

"""
# EOL qator yakunida hato bor
#print("Hello world")

# EOF funksiya yakunida hat









"""
Ro'yhatlar amaliy mashg'ulotlar
"""

# ismlar = []

# ismlar.append("Zafar")
# ismlar.append('Ozod')

# print(f"{ismlar[0]} bugun choyhona bormi \n{ismlar[1]} bugun choyhonaga borasanmi")


# sonlar = [-4, 2.3, 34, -15, 4.3]

# qoshish = sonlar[0]+sonlar[4]

# ayirish = sonlar[1]-sonlar[2]

# daraja = sonlar[3]**7

# print(f"sonlar ustida amallar: \n qo'shish {qoshish} \n ayirish{ayirish} \n darajaga ko'tarish {daraja}")

# t_shaxslar = ['Imom al-Buxoriy', 'Amir Temur', 'Jaloliddin Manguberdi']

# z_shaxslar = ['Ilon Musk', 'Mark Sukerberg', 'Jek Ma']

# print(f"Tarixiy shaxs {t_shaxslar[1]} bilan \nZamonaviy shaxslardan {z_shaxslar[1]} bilan suhbalashishni hohlardim ")

# friends = []

# friends.append('Sardor')
# friends.append('Zafar')
# friends.append('Javohir')
# friends.append('Ozod')
# friends.append('Doston')

# friends.remove('Doston')
# print(friends)
# friends.insert(0,'Fazliddin')
# friends.insert(5,'Humoyun')

# print(friends)

# mehmonlar = []

# mehmon_1 = friends.pop(0)
# mehmon_2 = friends.pop(4)
 
# mehmonlar.append(mehmon_1)
# mehmonlar.append(mehmon_2)

# print(f"choyxonada do'stlarim bilan o'tiribmiz {friends} \nchoyxonaga {mehmonlar} do'stlarim ham kelib qo'shildi")

"""
Ro'yhatlar ustida amallar
"""
davlatlar = ['O\'zbekiston', 'Nepal', 'Malayziya', 'Angilya', 'Italiya', 'Germaniya']

# print(davlatlar)

# uzun = len(davlatlar)

# print(uzun)

# tartib = sorted(davlatlar)

# teskari = sorted(davlatlar, reverse=True)

# print(f"Tartiblangan ro'yhat: {tartib} \nTeskari tartiblangan ro'yhat: {teskari}")

# davlatlar.reverse()

# print(davlatlar)

# davlatlar.sort()

# davlatlar.sort(reverse=True)

# print(davlatlar)

# juft_sonlar = list(range(120,1200,2))

# yigindi = sum(juft_sonlar)

# katta = max(juft_sonlar)
# kichik = min(juft_sonlar)
# print(juft_sonlar)
# print(yigindi)
# print(len(juft_sonlar))
# print(f"Katta son: {katta} \nKichik son: {kichik}")

# royhat_boshi = juft_sonlar[:20]

# royhat_ortasi = juft_sonlar[270:290]

# royhat_oxiri = juft_sonlar[520:]

# print(f"Ro'yhat boshi: {royhat_boshi} \nRo'yhat o'rtasi: {royhat_ortasi}\nRo'yhat oxiri: {royhat_oxiri}")

# taomlar = ['Tuxum', 'Sosiska', 'Yog\'', 'Osh', 'Do\'lma', 'Manti']

# nonushta = taomlar[:]

# del(nonushta[3:])

# nonushta.append('Non')
# nonushta.append('Shakar')

# print(f"Nonushta uchun ro'yhat: {nonushta}\nTaomlar ro'yhati: {taomlar}")

# nonushta = tuple(nonushta)

# nonushta.append('Fri')
# nonushta.append("Qaymoq")
# print(nonushta)
"""
For operatoriga oid misollar
"""
# ismlar = ['Javohir', 'Zafar', 'Shaxriyor', 'Bobur', 'Sardor', 'Doston']

# for ism in ismlar:
#     print(f"Assalomu alaykum {ism} xush kelibsiz")

# print(f"Kod {len(ismlar)} marta takrorlandi")

# sonlar = list(range(11,100,2))

# for son in sonlar:
#     print(f"{son} ning kubi {son**3} ga teng")
    
# kinolar = []

# for kino in range(5):
#     kinolar.append(input(f"{kino+1}-kino nomini kiriting:"))
# print(kinolar)
# a = int(input("Bugun nechta odam bilan suhbatlashdiz: "))

# odamlar = []

# for i in range(a):
#     odamlar.append(input(f"{i+1}-suhbatlashgan odamingiz kim:"))
# print(odamlar)

""" 
if elsega oid misollar 
"""
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

# foydalanuvchi_nomi = input("Loginni kiriting: ")
# parol = input("Parolni kiriting: ")

# if foydalanuvchi_nomi == "admin":
#     print("Xush kelibsiz, Admin")
# else: 
#     print(f"Xush kelibsiz, {foydalanuvchi_nomi}")

# son_1 = int(input("1-Butun sonni kiriting: "))

# son_2 = int(input("2-Butun sonni kiriting: "))

# if son_1 == son_2:
#     print("Sonlar teng!")
# else:
#     print("Sonlar teng emas!")

# son = int(input("Istalgan butun sonni kiriting: "))

# if son > 0:
#     print((son**(1/2)))
# else:
#     print("Musbat son kiriting!")
"""
if elif else ga oid misollar
"""
# son = int(input("Juft son kiriting: "))

# if son%2==0:
#     print("Rahmat!")
# else:
#     print("Bu juft son emas")

# yosh = int(input("Yoshingizni kiriting: "))

# if yosh>0:
#     if yosh<=4 or yosh >=60:
#         narh = 0 
#     elif yosh < 18:
#         narh = 10000
#     elif yosh >= 18:
#         narh = 20000
#     print(f"Sizga kirish {narh} so'm")
# else:
#     print("Noto'g'ri ma'lumot kiritingiz")
    
    
# mahsulotlar = ['anor', 'uzum', 'olma', 'ananas', 'banan', 'yogurt', 'fanta', 'tuxum', 'yog\'', 'shakar']

# savat = []

# for i in range(5):
#     savat.append(input(f"{i+1}-mahsulotni qo'shing: "))

# bor_mahsulot = []

# mavjud_emas = []

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulot.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print("Do'konimizda quydagi mahsulotlar mavjud emas!:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor!")


# foydalanuvchilar = ['damir', 'zafar', 'quvondiq', 'doston', 'anvar']

# login = input("yangi login tanlang: ")

# if login.lower() in foydalanuvchilar:
#     print("Xush kelibsiz!")
# else:
#     print("Login band, yangi login tanlang!")

# butun_son = int(input("Istalgan butun son kiriting: "))
# for bol in range(2,11):
#     if butun_son%bol==0:
#         print(f"{butun_son} soni {bol} ga qoldiqsiz bo'linadi")


"""
Lug'atlar mavzusida darslar
"""
# talaba_1 = {}

# talaba_1 ['ism'] = 'xolboyev damir'
# talaba_1 ['kurs'] = 4
# talaba_1 ['yosh'] = 26

# print(talaba_1)

# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# print(talaba_1)
# del talaba_1['yosh']
# print(talaba_1)


# otam = {'ismi' : 'Isoqov Abdurashid', 'tugilgan_yili' : 1964, }


# malumotlar = { 'damir': 'xolboyev',
#               'javohir': 'rustamov', 
#               'zafar': 'odiljonov', 
#               'quvondiq': 'kenjaboyev', 
#               'bobur': 'xolboyev',
#               'shaxriyor': 'xolboyev',
#               'jasur': 'qudratov',
#               'doston': 'o\'ktamov'
#               }

# for malumot in sorted(malumotlar.keys()):
#     print(malumot.title())
    
# for malumot1 in sorted(malumotlar.values()):
#     print(malumot1.title())


# davlatlar = {
#     'o\'zbekiston': 'toshkent',
#     'tojikiston': 'dushanbe',
#     'angilya': 'london',
#     'germaniya': 'berlin',
#     'kanada': 'ottava',
#     'xitoy': 'pekin',
#     'koreya': 'seul',
#     'yaponiya': 'tokiyo'
#     }
# for davlat1 in sorted(davlatlar.keys()):
#     print(davlat1.title())


# for davlat2 in sorted(davlatlar.values()):
#     print(davlat2.title())


# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# davlat = input('Davlat nomini kiriting: ').lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot mavjud emas")


    

# ismlar = []

# print("Yaqin do'stlaringizni ro'yhatini tuzamiz.")
# n=1
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n+=1
#     if javob != "ha" :
#         break

# print("Do'stilaringiz ro'yhati:")
# for ism in ismlar:
#     print(ism.title())

# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")







# x = "hello"

# #if condition returns True, then nothing happens:
# assert x == "hello"

# #if condition returns False, AssertionError is raised:
# assert x == "goodbye"



"""
FUNKSIYALAR
"""
# def salom_ber(ism):
#     """Foydalanuvchini ismini  qabul qilib 
#     Ism o'zgaruvchini qaytarib salom beradigan funksiya
#     """
#     print(f"Assalomu alaykum, hurmatli {ism.title()}")



# salom_ber("Damir")

# def tanishuvchi(yosh, ism):
#     """
#     Foydalanuvchini ismi va tug'ilgan yilini hisoblovchi funksiya
#     """
#     print(f"Assalomu alaykum {ism.title()}, siz {2023-yosh}-yilda tug'ilgansiz")


# ism = input("Ismingizni kiriting:")
# yosh = int(input("Yoshingizni kiriting:"))

# tanishuvchi(yosh,ism)

# def kvadrati(son):
#     """
#     Sonning kvadratini hisoblovchi funksiya
#     """
#     print(f"Kiritilgan sonning kvadrati {son**2}")


# son = int(input("Istalgan sonni kiriting: "))

# kvadrati(son)


# def avto_info (kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = { 'kompaniya': kompaniya,
#              'model': model, 
#              'rangi': rangi,
#              'korobka': korobka,
#              'yil': yili,
#              'narh': narhi      
#         }
#     return avto

# avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
# avto2 = avto_info('GM','Gentra', 'Oq', 'Mexanika', 2016, 15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar: ')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rangi']} {avto['model']}. Narh {narh}")



# def oraliq(min,max):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min+=1
#     return sonlar



# print(oraliq(0,13))
# print(oraliq(20,1651))

"""
dars davomida berilgan vazifa
"""

# def oraliq_1(min,max,qadam=1):
#     sonlar = []
#     while min < max:
#         if qadam > 1:
#             sonlar.append(min)
#             min+=qadam
#         else:
#             sonlar.append(min)
#             min+=1
#     return sonlar
    


# print(oraliq_1(23, 34, 2))

# print(oraliq_1(0,40))


# def avto_info (kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = { 'kompaniya': kompaniya,
#               'model': model, 
#               'rangi': rangi,
#               'korobka': korobka,
#               'yil': yili,
#               'narh': narhi      
#         }
#     return avto

# print("Saytimizdagi avtolar ro'yhatini shakillantiramiz.")
# avtolar=[]
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting", end='')
#     kompaniya=input("\nIshlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
    
    
#     #Foydalanuvchi kiritgan ma'lumotlardan avto.info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yhatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili,narhi))
    
#     #Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
    
# def user_info(famliya, ism, tugilgan_yili, manzil, email=None, tel_raqam=None):
#     user = {'famliya': famliya,
#             'ism': ism,
#             'tugilgan_yili': tugilgan_yili,
#             'manzil': manzil,
#             'email': email,
#             'tel_raqam': tel_raqam,
#             'yosh': 2023-tugilgan_yili
#         }
#     return user
    
# info1 = user_info('Xolboyev', 'Damir', 1997, 'Jizzax viloyati', 'xadmir97@gmail.com', '+998 91 194-24-24')
# info2 = user_info('Odiljonov', 'Zafar', 1997, 'Jizzax viloyati', 'zafar1811@mail.ru', '99891 196 11 18')

# print(f"Birinchi foydalanuvchining ma'lumotlari: \n{info1} \nIkkinchi foydalanuvchi ma'lumotlari: \n{info2}")
    
    
# print("Saytimizdagi foydalanuvchilar ro'yhati shakillantiramiz: ")
# user = []

# while True:
#     print("\nQuydagi ma'lumotlarni to'ldiring: ")
#     famliya = input("\nFamilyani kiriting: ")
#     ism = input("Ismni kiriting: ")
#     tugilgan_yili = int(input("tug'ilgan yilingizni kiritng: "))
#     manzil = input("Manzilingizni kiriting: ")
#     email = input("Elektron pochtani kiriiting: ")
#     tel_raqam = input("Telefon raqamni kiriting: ")
    
    
#     user.append(user_info(famliya, ism, tugilgan_yili, manzil, email, tel_raqam))
    
#     answer = input("Yana ma'lumot kiritmoqchimisiz? yes/no: ")
    
#     if answer == "no":
#         break

#Katta qiymat qaytaruvchi funksiya

# def uch_max(son1, son2, son3):
#     """
#     Uchta kiritilgan qiymatlardan eng kattasini aniqlovchi funksiya
#     """
#     if son1>son2 and son1>son3:
#         return son1
#     elif son2>son1 and son2>son3:
#         return son2
#     else:
#         return son3
    
    
    
    

# print(uch_max(23, 34, 33))



# def geo(radius, pi = 3.14):
#     aylana = { 'diametr' : radius * 2,
#               'perimetr' : radius * pi * 2,
#               'yuza' : 2 * pi * radius * radius
#         }
#     return aylana
    

# print(geo(10))



# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x - 1] + sonlar[x - 2])
#     return sonlar


# print(fibonacci(10))


def bahola (ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = int(baho)
    return baholar


# talabalar = ['damir', 'zafar', 'bobur', 'sardor']

# baholar = bahola(talabalar[:])
# print(baholar)

def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()   

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)

"""
Moslanuvchan funksiya
"""
def kopaytma(*sonlar):
    kop = 1
    for son in  sonlar:
        kop *= son
        
    return kop


# print(kopaytma(2,3,5,6,5))


def talaba_info(familya,ism, **talaba):
    talaba['familya'] = familya
    talaba['ism'] = ism
    return talaba

# talaba1 = talaba_info("Xolboyev", "Damir", t_yil = '28.02.1997')
# talaba2 = talaba_info("Odiljonov", "Zafar", t_yil = "18.11.1997", manzil = "Jizzax viloyati")











