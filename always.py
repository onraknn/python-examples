# Girilen degere kadar listeleyen program.
"""

list=[]
sayi=int(input("sayi giriniz : "))
for i in range(1,sayi+1):
    list.append(i)

print(list)
--------------------------------------------------------------------------------------------------------


"""

"""
# İF in kullanımı

isim ="onur"

if "o" in isim:
    print("isimde o harfi geçiyor")
else:
    print("isimde o hargi geçmiyor")



--------------------------------------------------------------------------------------------------------
"""


# String Örnekleri
""""
// işareti tam bölmeyi sağlar int tipinde alır.
** işareti üs almaya yarar print(5**2)  25

print("benim adım {}".format("onur"))
print("benim adım {}, yasim {} ".format("onur",21))
--------------------------------------------------------------------------------------------------------
"""

"""
cumle="merhaba onur nasılsın ?"
print(len(cumle))
print(cumle[0])
--------------------------------------------------------------------------------------------------------
"""

# iki değerin Toplamı
""""
a=input("lütfen 1. sayıyı giriniz :")
b=input("lütfen 2. sayıyı giriniz :")
toplam=float(a)+float(b)
print("girilen 2 sayinin toplamı :",toplam)
--------------------------------------------------------------------------------------------------------
"""

# Random
""" RASTGELE İYİ KÖTÜ
import random
print("nasılsın ?")

a=int(random.random()*100)

if a%2==0:
    print("iyiyim")
else:
    print("kötüyüm")
    --------------------------------------------------------------------------------------------------------
"""

# Dizi
"""
cities =["istanbul","tekirdağ","zonguldak","samsun","edirne"]
print(cities)
print(cities[2])
print(len(cities[2]))

cities.append("izmir")
print(cities)

cities.remove("tekirdağ")
print(cities)

del cities[1]
print(cities)

cities.insert(0,"zonguldak")
print(cities)

cities.sort()
print(cities)

print("antalya" in cities) #varmı diye bakıyoruz.
print("istanbul" in cities)

for city in cities:
    print(city)

for city in cities:
    print("gezilecek yerler :", city)
print("gezilecek yer kalmadı")
--------------------------------------------------------------------------------------------------------
"""

# Dizi
"""
str_cities="tokyo, denver, berlin"
my_list=str_cities.split(", ")
print(my_list)
print(str_cities)

str_cities2="karizma68472@gmail.com"
my_list2=str_cities2.split("@")
print("\n",str_cities2)
print(my_list2)
--------------------------------------------------------------------------------------------------------
"""

# For Range Kullanımı
"""
for number in range(1,10):
    print(number)

for ikiden in range(2,21,2):
    print(ikiden)

numara=list(range(1,11))
print(numara)

numbers =[number for number in range(1,11)]
print(numbers)
--------------------------------------------------------------------------------------------------------
"""

#liste
""" LİSTE
import random
number=[2,6,13,17,25,30]

print(number)
print("en küçüğü :",min(number))
print("en büyüğü :",max(number))
print("toplamları :",sum(number))

a=random.choice(number)
print("random",a)
--------------------------------------------------------------------------------------------------------
"""

#dizii uygulama
"""
dersler=["mat","fizik","kimya","ing","türk"]

print(dersler[1].upper())
print(dersler[4].upper())
print(dersler[4].lower())

print(dersler[1:3])
print(dersler[0:2])
print(dersler[-2:])
--------------------------------------------------------------------------------------------------------
"""

#dizi uygulama
"""
dersler=["mat",["fizik","kimya"],"ing","türk"]

print(dersler[1])
print(dersler[1][0])
print(dersler[1][1])

print(dersler[-1])
print(dersler[len(dersler)-1])
--------------------------------------------------------------------------------------------------------
"""

#dizi uygulama
"""
dersler=["mat","fizik","kimya","ing","türk"]

print(len(dersler))

dersler.append("tarih")
print(dersler)

dersler.insert(2,"cografya")
print(dersler)

del dersler[1]
print(dersler)

dersler.remove("mat")
print(dersler)
--------------------------------------------------------------------------------------------------------
"""

#dizi artan azalan
"""
numbers =[8,5,4,6,9,7,1,3,2,10]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
--------------------------------------------------------------------------------------------------------
"""

#dizi uygulama
"""
dersler=[["mat","fizik"],["kimya","ing"],["türk","tarih"]]
dersler2=[]
for ders in dersler:
    dersler2.append(ders[-1])

print(dersler2)
--------------------------------------------------------------------------------------------------------
"""

# For Range Kullanımı
"""
kare =[]
kare2=[]

for i in range(1,11):
    kare.append(i)
    kare2.append(i**2)

print(kare)
print(kare2)
--------------------------------------------------------------------------------------------------------
"""

""" kelimeyi harflerine ayırma
kelime=input("kelime gir : ")
sayac=0

while sayac<len(kelime):
    print(kelime[sayac])
    sayac+=1
else:
    print("kelimeyi ayırdım")
--------------------------------------------------------------------------------------------------------
"""

"""
pi = 3.14
r = float(input("yarı capı giriniz :"))
alan = pi * r * r
cevre = 2 * pi *r

greating = "alan : "+ str(round(alan,2))+ " cevre :"+str(cevre)
length = len(greating)

print(greating[0]) # 0. kararkter 

print(len(greating)) # kaç karakterli ise onu verir

print(greating[length-1]) #son karakter
--------------------------------------------------------------------------------------------------------
"""

"""
name = "onur"
surname = "akın"

print("benim adım {}, soyadım {}".format(name,surname)) # FORMAT KULLANIMI

print(f"benim adım {name}, soyadım {surname}") # F STRING KULLANILDI 
--------------------------------------------------------------------------------------------------------

"""

"""
x=list(range(1,11))

print(x)
print(x[2])
"""

"""

alfabe="asdfghjklşizxcvbnmöçqwertyuıopğü"

aranan=input("arananı gir : ")

if aranan in alfabe:
    print(aranan)
else:
    print("aranan yok !!")
"""

"""

dizi1="asdfghjklşizxcvbnmöç"
dizi2="qwertyuıopğhnkmsc"

for i in dizi1:
    if i in dizi2:
        print(i,end=" ")
"""


"""

fak=1
while True:
    sayi = int(input("faktöriyel hesaplanacak sayıyı gir : "))
    for i in range(1, sayi + 1):
      fak *= i
    print(fak)

"""
