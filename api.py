# import requests

# url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"


# answer = requests.get(url).json()
# # for money in answer:
# #     print(f"{money['Ccy']}------ {money['Rate']}******** {money['Diff']}>>>>>>>> {money['Date']}")

# eng_katta = answer[0]
# eng_kichik = answer[0]

# # Har bir valyuta bo'yicha solishtirish
# for money in answer:
#     rate = float(money['Rate'])

#     if rate > float(eng_katta['Rate']):
#         eng_katta = money

#     if rate < float(eng_kichik['Rate']):
#         eng_kichik = money

# # Natijani chiqarish
# print("\n✅ Eng yuqori kurs:")
# print(f"{eng_katta['Ccy']} - {eng_katta['Rate']} so'm (sana: {eng_katta['Date']})")

# print("\n✅ Eng past kurs:")
# print(f"{eng_kichik['Ccy']} - {eng_kichik['Rate']} so'm (sana: {eng_kichik['Date']})")

# def exchange_rate(money, quantity):
#     meney= money.upper()
#     for pul in answer: 
#         if pul.get('Ccy')==money:
#             dollar=pul['Rate']
#             hisob = quantity/float(dollar)
#             return hisob
#         return None            


# birlik = input('qanday pulga ayrboshlaysiz: ')
# miqdor = float(input('qnacha pulni ayrboshlaysiz: '))

# javob = exchange_rate(birlik,miqdor)
# print(javob)


# import requests

# url = "https://cbu.uz/en/arkhiv-kursov-valyut/json/"

# answer = requests.get(url).json()


# def exchange_rate(money, quantity):
#     money = money.upper()
#     for pul in answer:
#         if pul.get("Ccy") == money:
#             dollar = pul['Rate']
#             hisob = quantity/float(dollar)
#             return hisob
#     return None


# summa=[]
# for a in answer:
#     for k,v in a.items():
#         if k == 'Rate':
#             summa.append(v)
            
# javob=list(map(lambda x: float(x), summa))
# search = max(javob)

# for a in answer:
#     for k,v in a.items():
#         if v == str(search):
#             print(f"{a.get("Ccy")} {v} eng kattasi")

# # birlik = input("Qanday pulga ayr boshlaysiz: ")
# # miqdor = float(input("Qancha maydalaysiz: "))

# # javob = exchange_rate(birlik, miqdor)
# # print(javob)
# Python'da a.items() — bu lug‘at (dictionary) turidagi o‘zgaruvchi ustida ishlatiladigan metod. Uning vazifasi — lug‘atdagi har bir kalit (key) va qiymat (value) juftligini olish.

# Sintaksis:
# python
# Copy
# Edit
# a.items()
# Natija:
# Bu metod dict_items tipidagi obyektni qaytaradi, u esa ichida (kalit, qiymat) juftliklari bo‘lgan tuple lar to‘plamidan iborat bo‘ladi.

# Misol:
# python
# Copy
# Edit
# a = {'ism': 'Ali', 'yosh': 25, 'kasb': 'dasturchi'}

# for kalit, qiymat in a.items():
#     print(kalit, "->", qiymat)
# Natija:
# rust
# Copy
# Edit
# ism -> Ali
# yosh -> 25
# kasb -> dasturchi
# Bu juda qulay bo‘lib, lug‘at ichidagi ma'lumotlarni kalit va qiymat bilan ajratib olish imkonini beradi.