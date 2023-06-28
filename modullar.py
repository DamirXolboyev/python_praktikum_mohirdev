# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 14:54:43 2023

@author: xdamir
"""
import random as r

ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
print(ism)
print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz
x = list(range(0,51,5))
print(x)
print(r.choice(x))