# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 06:52:37 2023

@author: xdamir
"""
#String mavzusiga oid vazifalar
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

#son_1 = float(input("Birinchi sonni kiriting: "))

#son_2 = float(input("Ikkinchi sonni kiriting: "))

#qoshish = son_1 + son_2
#ayirish = son_1 - son_2
#kopaytirish = son_1 * son_2
#bolish = son_1 / son_2

#print(f"{son_1} + {son_2} = {qoshish}\n {son_1} - {son_2} = {ayirish}\n {son_1} * {son_2} = {kopaytirish}\n {son_1} + {son_2} = {bolish}\n")

son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
