# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 06:52:37 2023

@author: xdamir
"""

kocha = input("Ko'chani kiriting: ")
mahalla = input("Mahallani kiriting: ")
tuman = input("Tumanni kiriting: ")
viloyat = input("Viloyatni kiriting: ")

manzil = f"{kocha} ko\'chasi {mahalla} mahallasi {tuman} tumani {viloyat} viloyati"

katta_harf = manzil.upper()

kichkina_harf = manzil.lower()

bosh_harf_katta = manzil.title()

faqat_bosh_harf_katta = manzil.capitalize()

print(manzil)

print(katta_harf, kichkina_harf, bosh_harf_katta, faqat_bosh_harf_katta)

print(f"{kocha} ko\'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati")

