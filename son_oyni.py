# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:26:07 2023

@author: xdamir
"""
import random as r
def son_top (son=10):
    tasodifiy = r.randint(0,son)
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
            