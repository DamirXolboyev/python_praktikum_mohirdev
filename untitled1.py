# meva = "     olma     "
# print("Men " + meva.lstrip() + " yaxshi ko'raman")
# print("Men " + meva.rstrip() + " yaxshi ko'raman")
# print("Men " + meva.strip() + " yaxshi ko'raman")
# print("Men " + meva + " yaxshi ko'raman")

# ism = input("Ismingizni kiriting:")

# print(f"Assalomu alaykum, {ism}")

# yosh = int(input("Yoshingizni kiriting:"))

# print(f"Sizni yoshingiz, {yosh}")



# son_1 = 324
# son_2 = 4132
# kopaytir = son_1 * son_2

# bolish = son_2 // son_1
# kvadrat = son_1 ** 5
# qoldiq = son_2 % son_1
# print(qoldiq)



katta_son = 10_000_000
#1.1 foydalanuvchining tug'ilgan yilini so'raymiz
t_yil = input("Tug'ilgan yilingizni kiriting: ")
#1.2 t_yil o'zgaruvchini int ga aylantiramiz
t_yil = int(t_yil)
#2 foydalanuvchi yoshini xisoblaymiz
yosh = 2023 - t_yil # 
#3 foydalanuvchi yoshini konsolga chiqaramiz
print("Siz " + str(yosh) + " yoshda ekansiz")