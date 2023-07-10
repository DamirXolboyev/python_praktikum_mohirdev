# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:26:07 2023

@author: xdamir
"""
import random as ran
def son_top (son=10):
    tasodifiy = ran.randint(0,son)
    print(f"Men 1 dan {son}gacha son o'yladim. Topa olasizmi:")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if tasodifiy > taxmin:
            print("Xato, Men o'ylagan son kattaroq, Yana xarakat qiling:")
        elif tasodifiy < taxmin:
            print("xato, Men o'ylagan son kichikroq, Yana xarakat qiling:")
        else:
            break
    print(f"Tabriklaymiz. {taxminlar} taxmin bilan topdingiz!")
    return taxminlar


def son_top_pc(x=10):
    print(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = ran.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"Men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print("Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar
def play(x=1):
    yana = True
    while yana:
        taxminlar_user = son_top(x)
        taxminlar_pc = son_top_pc(x)
        
        if taxminlar_user > taxminlar_pc:
            print("Men yutdim!")
        elif taxminlar_pc > taxminlar_user:
            print("Siz yutdingiz!")
        else:
            print("Durrang!")
                
        yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0)"))
        