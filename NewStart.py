#
# sayi1 = int(input("sayi1 gir : "))
# sayi2 = int(input("sayi2 gir : "))
# toplam = sayi2+sayi1
# print("toplam :",toplam)
#
#
#
# name = 'onur'
# surname = "AKIN"
# age = 22
# write ="My name is "+name+" "+surname+" i am "+str(age)+" years old."
# length = len(write)
#
# print(write)
# print(length)
# print(write[length-1])
#
# result = 200/700
# result2 = 200/500
# r = result2+result
# print("result : {r:1.3} + {r2:1.3} : {r3:1.3}".format(r=result,r2=result2,r3=r))
#
# #print('my name is {} i am {} years old'.format(name,surname))
#
#
#
#
# #---------------------------------------------------------EXAMPLES----------------------------------------------------------------------------
#
#
#
# website = "https://www.sadikturan.com"
# course = "Pythomn kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
#
# print(len(course))
#
# print(website[8:11])
#
# print(course[:15]+course[-15:-1])
#
# print(course[-1:len(course)*-1-1:-1])
#
# name = "Hello world"
# print(name.replace("o","W"))
#
# x = "abc"
# print(x*3)
#
#
#
#
#
# liste = "deneme merhaba onur".split()
# print(liste[1])
#
# dizi = [1,2,3,4,5]
# print(dizi)
#
# list = ["onur","akın"]
# print(list[1])
#
# l1 = ["ali",20]
# l2 = ["veli",30]
# l3 = [l1 , l2]
#
# print(l3)
# print(l3[1])
# print(l3[1][0])
#

# liste = [1,2,3]
# liste2 = ["onur","akın"]
#
# print(liste[0])
# print(liste2[1])


#liste içi tipini öğrenme---------
#
# liste = ["onur",12,12.5,[10,20,30,40]]
# print(liste[3][0])


# liste = ["ali","ayse","veli"]
#
# liste.append("onur")
# print(liste)
#
# liste.remove("ayse")
# print(liste)
#
# liste.insert(2,"onur")
# print(liste)
#
# a = liste.count("onur")
# print(a)
#
# liste_yedek = liste.copy()
# print(liste_yedek)
#
# liste.extend([10,20,30])
# print(liste)
#
# b = liste.index(10)
# print(b)
#
# liste.reverse()
# print(liste)
#
# liste1 = [10,20,30,4,50]
# liste1.sort()
# print(liste1)
#
# liste1.clear()
# print("liste 1 silindi",liste1)


#tuple-------

# t = ("ali","veli",1,2,3.5,[1,2,3])
# print(t[1])


#dictionary(sözlük)---------

# dic ={
#     1: {"onur": 1,
#         "akın": 2},
#     2: {"onur": 1,
#         "akın": 2},
#     3: {"onur": 1,
#         "akın": 2}
# }
# print(dic)
# print(len(dic))
# print(dic[1])

#fonksiyon ------
#
# def carp(a,b=1):
#     return a**b
# print("cikti",carp(2))
#
#
# liste = []
# def eleman_ekle(a):
#     liste.append(a)
#
# print(eleman_ekle(2))
# print(liste)
# print(eleman_ekle(3))
# print(liste)


#for-def örneği

# def new_wage(x):#yeni maaş
#     return int(x*0.20)+x
#
# maaslar =[1000,2000,3000,4000,5000]
#
# for i in maaslar:
#     print(new_wage(i))


#nesne yönelimli programlama - classs yapıları -------------------

# class veri_bilimci():
#     bolum = ""
#     sql = "evet"
#     deneyim_yili = 0
#     bildigi_diller = []
#
# print(veri_bilimci.sql)
#
# veri_bilimci.sql = "hayir"
#
# print(veri_bilimci.sql)
#
# ali = veri_bilimci()
# print(ali.sql)
# print(ali.deneyim_yili)
#
# ali.bildigi_diller.append("python")
# print(ali.bildigi_diller)
#
# veli = veri_bilimci()
# print(veli.sql)
# print("veli",veli.bildigi_diller[0],"bilmemeliydi")
#



# #-------------------------------------------------LİST EXAMPLES-----------------------------------------------------------------------------
#
# liste = ["bmw","mercedes","opel","mazda"]
#
# print(len(liste))
#
# print(liste[0], liste[-1])
#
# liste[3] = "toyota"
# print(liste)
#
# result = "mercedes" in liste
# print(result)
#
# print(liste[-2])
#
# print(liste[0:3])
#
# liste[-2] = "toyota"
# liste[-1] = "renault"
# print(liste)
#
# result = liste + ["nissan","fiat"]
# print(result)
#
# del liste[-1]
# print(liste)
#
# print(liste[::-1])
#
#
#
#
# numbers = [1,10,5,16,4,9,10]
# letters = ["a","g","s","a","y","a","s"]
#
# print(min(numbers))
# print(max(numbers))
#
# print(min(letters))
# print(max(letters))
#
# print(numbers[3:6])
#
# print(numbers)
#
# numbers.append(49)
# print(numbers)
#
# numbers.insert(3,20)
# print(numbers)
#
# numbers.pop()
# print(numbers)
#
# numbers.remove(5)
# print(numbers)
#
# numbers.sort()
# print(numbers)
#
# numbers.reverse()
# print(numbers)
#
# print(len(numbers))
#
# print(numbers.count(10))
#
# print(letters.count('a'))
#
# numbers.clear()
# print(numbers)
#
#
#
#
# #-------------------------------------------------LİST EXAMPLES-------------------------------------------------------------------------------
#
# names = ["Ali","Yağmur","Hakan","Deniz"]
# years = [1998,2000,1998,1987]
#
# names.append("cenk")
# print(names)
#
# names.insert(0,"Senna")
# print(names)
#
# print(names.index("Deniz"))
#
# names.remove("Deniz")
# print(names)
#
# value = "Ali" in names
# print(value)
#
# names.reverse()
# print(names)
#
# names.sort()
# print(names)
#
# years.sort()
# years.reverse()
# print(years)
#
# str = "Chevrolet,Dacia".split(",")
# print(str)
#
# print(min(years))
#
# print(max(years))
#
# years.clear()
# print(years)
#
# marka = []
# m1 = input("1. markayı gir : ")
# marka.append(m1)
# m2 = input("1. markayı gir : ")
# marka.append(m2)
# m3 = input("1. markayı gir : ")
# marka.append(m3)
#
# print(marka)
#
#
#
# list = ["ahmet","mehmet"]
# tuple = ("özge","sude")
#
# print(list)
# list[0] = "onur"
# print(list)
#
# #tuple[0] = "rabia"
# #tuple değer eklendikten sonra değiştirilemez fakat yeni bir liste yapılabilir.
# print(tuple)
#
#
#
# sehirler = ["istanbul","tekirdağ"]
# plakalar = [34,59]
# print(plakalar[sehirler.index("tekirdağ")])
# print(sehirler[plakalar.index(34)])
#
# cars = {"bmw": 1,"mercedes ": 2,"lexus": 3}
# print(cars["bmw"])
# cars["ferrari"] = 6
# cars["lexus"] = 5
# print(cars)
#
#
#
# users = {
#     "onur": {"years":2000,
#              "age":21,
#              "star sign" :"akrep"
#              },
#     "akın": {"years":2002,
#              "age":19,
#              "star sign" :"kova"
#              },
#     "ahmet": {"years":2001,
#               "age":20,
#               "star sign" :"terazi"
#               },
#     "mehmet": {"years":1999,
#                "age":22,
#                "star sign" :"aslan"}
# }
# print(users)
# print(users["onur"])
# print(users["onur"]["age"])
#
#
# ogrenciler = {}
#
# ogr_no = input("ogrenci no : ")
# ad = input("ad : ")
# soyad = input("soyad : ")
# telefon = input("telefon : ")
#
#
# ogrenciler[ogr_no] = {
#             "ad": ad,
#             "soyad":soyad,
#             "telefon":telefon
# }
#
#
#
# print(ogrenciler)
#
# ogrenciler.update({
#    ogr_no: {
#         "ad": ad,
#         "soyad":soyad,
#         "telefon":telefon
#    }
# })
# print(ogrenciler)
#
#
# karşılaştırma operatörleri -----------------------------------------------------------------------------------------------------------------
#
#
# users = "onr_aknn"
# password = "123"
#
# u = input("kullanıcı adını gir : ")
# p = input("şifreni gir : ")
#
# if(users == u and password == p):
#     print("giriş başarılı")
# else:
#     print("giriş başarısız")
#
# vize1 = int(input("1. vizeyi gir : "))
# vize2 = int(input("2. vizeyi gir : "))
# final = int(input("1. finali gir : "))
#
# ortalama = ((vize1+vize2)*60/100) + (final*40/100)
#
# if(ortalama < 50 or final < 50):
#     print("kaldınız !!!")
#
# if(final>=70):
#     print("geçtiniz !!!")
#
#
# name = input("isim gir : ")
# age = int(input("yas gir : "))
# deger = int(input("egitim bilgileri \n1-Lise\n2-Üniversite\n3-Diger\n"))
#
# if(age>17 and (deger == 1 or deger == 2)):
#     print("ehliyet alabilrisin")
# else:
#     print("ehliyet alamazsın")

#
#
#
# list = ["muhammed","akın","onur"]
#
# for i in list:
#     print(f'merhaba benim ismim {i}')
#
# tuple = ((1,2),(3,4),(5,6))
#
# for i,j in tuple:
#     print(i,j)
#
# dictionary = {
#     "1":{"a":3,"b":5},
#     "2":{"a":0,"b":8},
#     "3":{"a":9,"b":6}
# }
#
# for i in dictionary:
#     print(i)
#
# for i in dictionary.items():
#     print(i)
#
#
# Çalışma-----------------------------------------------------------------------------------------------------------------------------------------
#
#
# sayilar = [1,3,5,7,9,12,19,21]
# toplam =0
#
# for i in sayilar:
#     if(i%3==0):
#         print(i)
#
# for i in sayilar:
#     toplam +=i
# print(toplam)
#
# for i in sayilar:
#     if(i%2==1):
#         print(i*i)
#     else:
#         print(i)
#
# print()
#
#
# sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]
#
# for i in sehirler:
#     if(len(i)<=5):
#         print(i)
#
#
# print()
#
# urunler = [
#     {"name": "s6", "price" : "3000"},
#     {"name": "s7", "price" : "4000"},
#     {"name": "s8", "price" : "5000"},
#     {"name": "s9", "price" : "6000"},
#     {"name": "s10", "price" : "7000"},
# ]
#
# count = 0
#
# for i in urunler:
#     count += int(i["price"])
#     if(int(i["price"])<5000):
#         print(i["name"])
#
# print(count)
#
#
#
# i = 0
# while i<100:
#     print(i)
#     i+=1
#
#
# random = 0
# while True:
#     sayi = int(input("gir: "))
#     if sayi == random:
#         print("helal")
#         break
#
#
#
# name = "onur"
# tahmin = input("isim gir : ")
# while True:
#
#     if tahmin == name:
#         print("doğru girdiniz")
#         break
#     tahmin = input("tekrar gir : ")
#
#
#
# UYGULAMA---------------------------------------------------------------------------------------------------------------------
#
# sayilar =[1,3,5,7,9,12,19,21]
# i=0
# while True:
#     print(sayilar[i])
#     i+=1
#     if i==len(sayilar):
#         break
#
#
# baslangic = int(input("baslagic degerini gir : "))
# bitis = int(input("bitis degerini gir : "))
#
# while True:
#     print(sayilar[baslangic-1])
#     baslangic+=1
#     if baslangic> bitis:
#         break
#
#
# i=100
# while i>0:
#     print(i)
#     i-=1
#
#
# i=0
# j=0
# dizi =[]
#
# while i!=5:
#    dizi.append(int(input(f"{i+1}. sayiyi gir : ")))
#    i += 1
#
# dizi.sort()
# print(dizi)



# urunler = []
# adet = int(input("kaç ürün eklemek istersiniz : "))
#
# i = 0
#
# while i<adet:
#     name = input("ürün ismi : ")
#     price = int(input("ürün fiyatı : "))
#     urunler.append({
#         "name": name,
#         "price": price
#     })
#     i+=1
#
# for i in urunler:
#     print(i)


# toplam =0
# i=0
# while i<100:
#     i += 1
#     if i%2==1:
#         toplam+=i
#
# print(toplam)


# yazi = "hello there"
# index=1
# for i in yazi:
#     print(f"index : {index} harf : {i}")
#     index+=1


# yazi = "hello"
#
# for i,j in enumerate(yazi):
#     print(f" i : {i} j : {j}")



# liste1 = [1,2,3,4,5]
# liste2 = ["a","b","c","d","e"]
#
# a = list(zip(liste1,liste2))
# print(a)
# print(a[2])
# print(a[2][0])





# import random
#
# rastgele = random.randint(1,100)
# maxPuan = 100
# hak = int(input("hak degerini giriniz : "))
# puan = 100/hak
# i=0
# print(rastgele)
# while True:
#     i+=1
#     sayi = int(input(("tahmin edilen {0}. sayiyi gir : ").format(i)))
#
#     if sayi>rastgele:
#         print("İn")
#         hak-=1
#         maxPuan-=puan
#     elif sayi<rastgele:
#         print("Çık")
#         hak -= 1
#         maxPuan -= puan
#     else:
#         print("doğru tahmin ettiniz tebrikler.")
#         print("puan : ",round(maxPuan,1))
#         break
#
#     if hak==0:
#         print("hak kalmadı sayi = ",rastgele)
#         print("puan = 0")
#         break



# sayi = int(input("bir sayi gir : "))
#
# if sayi>1:
#
#     for i in range(2,sayi):
#
#         if sayi%i==0:
#             print("asal sayi değil ! ")
#             break
#     else:
#         print("asal sayidir")
# else:
#     print("asal sayi değildir")



#palindrom sayi bulma

#
# kelime = input("bir kelime gir : ")
# ters =""
#
# for i in range(-1, len(kelime)*-1-1,-1):
#     ters += kelime[i]
#
# if ters==kelime:
#     print("palindrom")
# else:
#     print("palindrom değil")
#


# sesli = "AEIOUÜÖİaeiıoüöu"
# metin = input("metin gir : ")
# count =0
#
# for i in sesli:
#     if i in metin:
#         count+=1
#
# print("toplam : ",count)



# sayi = int(input("faktöriyeli alınacak sayi gir : "))
# fak = 1;
#
# if sayi<0:
#     print("negatif sayi girilemez ")
#
# elif sayi==0:
#     print("faktöriyel = 1")
# else:
#
#     for i in range(1,sayi+1):
#         fak *=i
#
#     print(fak)


# ilk = 0
# son = 1
#
# sayi = int(input("kaç adet finonacci sayisi gösterilsin : "))
#
# print("0 1 ",end="")
#
# for i in range(1,sayi-1):
#     toplam = ilk+son
#     print(toplam,end=" ")
#     yedek = ilk
#     ilk = son
#     son = toplam


#
# toplam =0
# sayi = int(input("sayi gir : "))
#
# for i in range(1,sayi+1):
#     toplam += pow(i,3)
#
# print(toplam)


#
# sayi = int(input("sayi gir : "))
#
# if sayi>1:
#     for i in range(2,sayi):
#         if sayi%i==0:
#             print("sayi asal değildir")
#             break
#     else:
#         print("sayi asaldır")
#
# elif sayi==1 or sayi==0:
#     print("asal değildir ")
# else :
#     print("negatif değer girilemez")


# Klavyeden aralarına virgül konularak yazılan tüm sayıları toplayan python kodunu yazınız.
#
# toplam = 0
#
# a=input("aralara virgül kullanarak sayilar gir (1,2,3,4,5) : ")
# print(a)
# list = a.split(',')
# print(list)
#
# for i in list:
#     toplam+=int(i)
#
# print("toplam = ",toplam)

#
# #0 dan 100 e kadar olan tek sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.
# a=1
# toplam =0
# while a<100:
#     toplam+=a
#     a+=2
# print(toplam)


# # rakamlarının toplamı 3 basamaklı
#
# sayi = int(input("sayi gir: "))
#
# yb = int(sayi/100)
# bb = int(sayi%10)
# ob = int(sayi%100)
# ob = int(ob/10)
#
# print(yb,ob,bb)
# print(yb+ob+bb)


# #tarih
# import datetime
# print(datetime.datetime.now())
#
# import time
# print(time.ctime())


# saniye = int(input("Saniye Giriniz:"))
# saat = saniye // 3600  # 1saat 3600 saniyeye eşittir.
# saniye = saniye % 3600
# dakika = saniye // 60
# saniye = saniye % 60
# print("Girdiğiniz Saniyenin Saat Dönüşümü:", saat, "sa", dakika, "dk", saniye, "sn")
#




#
# enBuyuk = 0
# list =[]
# sayi = int(input("kaç adet sayi girmek istersiniz : "))
#
# for i in range(0,sayi):
#     list.append(int(input(f"{i+1}. sayiyi gir : ")))
#
#     if list[i]>enBuyuk:
#         enBuyuk=list[i]
#
# print("en buyuk sayi = ",enBuyuk)



# a = int(input("x : "))
#
# for i in range(0,a+1):
#     for j in range(0,i):
#         print(end="*")
#     print()


# for i in range(0,5):
#     print("*"*i)
# print("\n")

#
#
# basamak = 0
#
# sayi = float(input("sayi gir : "))
#
# bb=int(sayi%10)
# ob =sayi/10
# ob= int(ob%10)
# yb=int(sayi/100)
#
#
# while sayi>1:
#     sayi = sayi/10
#     basamak+=1
#
# print("adet : ",basamak)
# print(ob)
# print(bb)
# print(yb)
#
# if basamak==(ob+yb+bb):
#     print("eşit")
# else:
#     print("eşit değil")
#


# s1 = int(input("1. gir : "))
# s2 = int(input("2. gir : "))
# t=0
#
# for i in range(0,s1):
#     t+=s2
#
# print(t)

# satir = int(input("satir gir : "))
# sutun = int(input("sutun gir : "))
#
# matris1 = [[0 for i in range(0,sutun)] for j in range(0,satir)]
# matris2 = [[0 for i in range(0,sutun)] for j in range(0,satir)]
# matris3 = [[0 for i in range(0,sutun)] for j in range(0,satir)]
# matris4 = [[0 for i in range(0,sutun)] for j in range(0,satir)]
#
# print("\n1. MATRİS\n")
# for i in range(0,satir):
#     for j in range(0,sutun):
#         matris1[i][j]=input(f'{i+1}. satır {j+1}. sutunu gir : ')
#
# print("\n2. MATRİS\n")
# for i in range(0,satir):
#     for j in range(0,sutun):
#         matris2[i][j]=input(f'{i+1}. satır {j+1}. sutunu gir : ')
#
# for i in range(0,satir):
#     for j in range(0,sutun):
#         matris3[i][j]=int(matris1[i][j])+int(matris2[i][j])
#
# print()
# print(matris1)
# print(matris2)
# print("\nMATRİSLERİN TOPLAMI\n")
# print(matris3)
#
# print("\nMATRİSLERİN ÇARPIMI")
#
# for i in range(0,satir):
#     for j in range(0,sutun):
#         for k in range(0,sutun):
#             matris4[i][j] += int(matris1[i][k])*int(matris2[k][j])
#
# print(matris4)

# #5in kuevveti mi
# i=1
# sayi = int(input("sayi gir : "))
#
# while True:
#
#     if sayi%pow(5,i)==0:
#         print("5 in kuveetidir.")
#         break
#     elif sayi%pow(5,i)< sayi:
#         i+=1
#     else :
#         print("5 in kuvveti değildir")
#         break

#
# #dost sayı
# xtop=0
# ytop=0
#
# x = int(input("x sayisini gir : "))
# y = int(input("y sayisini gir : "))
#
# for i in range(1,x):
#     if x%i==0:
#         xtop+=i
#
#     if y % i == 0:
#         ytop += i
#
# if ytop==x and xtop==y:
#     print("dost sayı")
# else:
#
#     print("değil")



# #mükemmel sayı
#
# sayi = int(input("sayi gir : "))
# t=0
# for i in range(1,sayi):
#     if sayi%i==0:
#         t+=i
# if t==sayi:
#     print("mukemmel sayi")
# else:
#     print("mukemmel değil")


# onluktan ikiliğe geçiş

# kalan = 0
# dizi = []
#
# sayi = int(input("sayi gir : "))
#
# while sayi>=1:
#     kalan = sayi%2
#     sayi = sayi/2
#     dizi.append(int(kalan))
#
# print(dizi)



# #ikilik ten onluğa geçiş
#
# onluk = 0
# sayi = input("binary değer gir (10010): ")
#
# for i,j in zip(range(len(sayi)-1,-1,-1 ), range(0, len(sayi))):
#     onluk+=int(sayi[j])*int(pow(2,i))
#
# print(onluk)


# ebob ekok
#
# eb=0
# ebob=1
# ekok=1
#
# s1 = int(input("s1 gir : "))
# s2 = int(input("s2 gir : "))
#
# ekok = int((s1*s2))
#
# for i in range(1,s1+1):
#     if s1%i==0 and s2%i==0:
#         s1/=i
#         s2/=i
#         ebob *= i
#
# ekok = int(ekok/ebob)
#
# print("ebob = ",ebob)
# print("ekok = ",ekok)


#DEF KULLANIMIIIIIIIIIIIIIIIIIIIII

#
# def Inceptions():
#     print("başlangıç")
# Inceptions()
#
#
# name = input("isim gir : ")
# def deneme(name):
#     print("merhaba "+name)
# deneme(name)
#
#
# years= input("yaşını gir : ")
# def new(years):
#     return "yaşım "+years
# a = new(years)
# print(a)
#


# asal sayı bulan program
#
# sayi = int(input("sayi gir : "))
#
# for i in range(2,sayi):
#     if sayi%i==0:
#         print("asal değil")
#         break
# else:
#     print("asal")
#



# eb = 0
# yedek = 0
# dizi = []
# eleman =0
#
# for i in range(0,5):
#     dizi.append(int(input(f"{i+1}. elemanı gir : ")))
#
# print()
#
# for i in range(0, len(dizi)):
#     if eb < dizi[i]:
#         eb = dizi[i]
#
# for i in range(0,len(dizi)):
#     if dizi[i]!= eb:
#         eleman+=1
#     else:
#         break
#
# print("girilen dizi = ",dizi)
#
# for i in range(0,5):
#     for j in range(0,5):
#         if dizi[i]>dizi[j]:
#             yedek = dizi[i]
#             dizi[i]=dizi[j]
#             dizi[j]=yedek
#
# print("en büyük elemanın sırası = ",eleman+1)
# print("büyükten küçüğe = ",dizi)
# print("en büyük eleman : ",eb)


#
# #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# dizi = []
#
# eleman = int(input("kaç eleman gireceksiniz : "))
#
# for i in range(0,eleman):
#     if i%2==0:
#         dizi.insert(i,input(f"{i+1}. elemanı gir : "))
#     else:
#         dizi.insert(len(dizi)-i, input(f"{i + 1}. elemanı gir : "))
#
# dizi.reverse()
# print(dizi)



# #aranan kelimeden kaç adet olduğunu bulan program
# adet =0
# yazi = "merhaba onur nasılsın"
# kelime = input("aranan harfi gir : ")
#
# for i in range(0, len(yazi)):
#     if kelime in yazi[i]:
#         adet+=1
#
# print(f"{adet} adet var")



# #polindrom kelime bulma
#
# kelime = input("kelime gir : ")
#
# if kelime==kelime[::-1]:
#     print("polindrom")
# else:
#     print("değil")


#
# bos =0
# dizi = []
# adet = int(input("kaç adet sayi giriceksiniz : "))
#
# for i in range(0,adet):
#     dizi.append(int(input(f"{i+1}.sayiyi gir :  ")))
#
# for i in range(0, len(dizi)):
#     for j in range(i+1,len(dizi)):
#         if dizi[i]>dizi[j]:
#             bos = dizi[i]
#             dizi[i]=dizi[j]
#             dizi[j] = bos
# print(dizi)
# print("en büyük 2. eleman : ", dizi[len(dizi)-2])




# a =0
# dizi = []
# ayni = []
#
# adet = int(input("kaç adet sayi girilecek : "))
#
# for i in range(0,adet):
#     dizi.append(int(input(f"{i+1}. elemanı gir : ")))
#
# for i in range(0,adet):
#     for j in range(i+1,adet):
#         if dizi[i]==dizi[j]:
#             print(i,j)
#             ayni.append(j)
#             if j in ayni:
#                 break
#
# print("eski dizi :",dizi)
#
# for i in range(0, len(ayni)):
#     print(f"{ayni[i]}. silindi")
#     dizi.pop(ayni[i]-a)
#     print(dizi)
#     a+=1
#
# print("aynı olanlar : ",ayni)
# print("yeni dizi :",dizi)


#
# yedek =0
# matris1 = [[0 for i in range(0,2)] for j in range(0,2)] # değerleri for ile girilecek matris
#
# for i in range(0,2):
#     for j in range(0,2):
#         matris1[i][j]=input(f'{i+1}. satır {j+1}. sutunu gir : ')
#
# print("eski : ",matris1)
#
# for i in range(0,2):
#     for j in range(0,2):
#         if i != j:
#             yedek = matris1[i][j]
#             matris1[i][j] = matris1[j][i]
#             matris1[j][i] = yedek
#     break
# print("yeni : ",matris1)




# yedek =0
#
# satir = int(input("satir sayisini gir : "))
# sutun = int(input("sutun sayisini gir : "))
#
# matris1 = [[0 for i in range(0,sutun)] for j in range(0,satir)] # değerleri for ile girilecek matris
# matris2 = [[0 for i in range(0,satir)] for j in range(0,sutun)] # değerleri for ile girilecek matris
#
# for i in range(0,satir):
#     for j in range(0,sutun):
#         matris1[i][j]=input(f'{i+1}. satır {j+1}. sutunu gir : ')
#
# print("eski : ",matris1)
#
# for i in range(0,satir):
#     for j in range(0,sutun):
#         matris2[j][i] = matris1[i][j]
#
# print("yeni : ",matris2)



#params komutu (istenildiği kadar parametre alır)
#
# def topla(*params):
#     return sum(params)
#
# a = topla(1,2,3)
# b = topla(1,2,3,4)
#
# print(a)
# print(b)




# --------------------------------def fonksiyon örnekleri----------------------------------
# 1.

# def isim(name):
#     return name
#
# kelime = input("kelime gir : ")
# adet = int(input("kaç adet girilecek : "))
#
# for i in range(0,adet):
#     print(isim(kelime))

# 2.



# 3.

# def asal(s1,s2):
#     for sayi in range(s1, s2 + 1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if (sayi % i) == 0:
#                     break
#             else:
#                 print(sayi)
# asal(2,10)


#4. fonksiyon kullanarak tam bölenleri liste içine alma programı

# def bolen(sayi):
#     liste = []
#     for i in range(1,sayi+1):
#         if sayi%i==0:
#             liste.append(i)
#     return liste
#
# print(bolen(10))


#yarı yarıya bölme yöntemi

#aralık = [2,4] a=2 ve b=4
#
# x = float(0) # anın değeri
# y = float(1)  # bnin değeri
# i=0 # iterasyın sayısı
# E=100
# kok =0 # kök değeri
#
# def denklem(sayi):
#     return sayi-pow(2,-sayi)
#
# def x0(a,b):
#     return (a+b)/2
#
# def hata(a,b):
#     c = (a-b)/2
#     if c<0:
#         c = c*-1
#     return c
#
# while E>pow(10,-5):
#     i+=1
#     a = float(denklem(x))
#     b = float(denklem(y))
#
#     if (a*b) < 0:
#         x_yeni = x0(x,y)
#         c = denklem(x_yeni)
#         if c >0:
#             if denklem(x) < 0:
#                 E = hata(x, y)
#                 print(f"{i}. iterasyon : x = {round(x,5)} , y = {round(y,5)} , hata = {round(E,5)} ")
#                 x = x
#                 y = x_yeni
#
#             if denklem(y) < 0:
#                 E = hata(x, y)
#                 print(f"{i}. iterasyon : x = {round(x,5)} , y = {round(y,5)} , hata = {round(E,5)} ")
#                 x = x_yeni
#                 y = y
#         if c < 0:
#             if denklem(x) > 0:
#                 E = hata(x, y)
#                 print(f"{i}. iterasyon : x = {round(x,5)} , y = {round(y,5)} , hata = {round(E,5)} ")
#                 x = x
#                 y = x_yeni
#
#             if denklem(y) > 0:
#                 E = hata(x, y)
#                 print(f"{i}. iterasyon : x = {round(x,5)} , y = {round(y,5)} , hata = {round(E,5)} ")
#                 x = x_yeni
#                 y = y
#
#     elif (a*b)>0:
#         print("kök tanımlı değil")
#     else:
#         print(f"kök : {a} ve {b} 'dir.")
#




# lineer interpolasyon

# x = 0 # anın değeri
# y = 1  # bnin değeri
# i=0 # iterasyın sayısı
# E=100
# kok =0 # kök değeri
#
# def denklem(sayi):
#     return sayi-(pow(2,-sayi))
#
# def x0(a,b):
#     return ((b*denklem(a))-(a*denklem(b)))/(denklem(a)-denklem(b))
#
# def hata(a,b):
#     c = (a-b)/2
#     if c<0:
#         c = c*-1
#     return c
#
# while E>0.00001:
#     i+=1
#     a = denklem(x)
#     b = denklem(y)
#
#     if (a*b) < 0:
#         x_yeni = x0(x,y)
#         c = denklem(x_yeni)
#         if c > 0:
#             if denklem(x) < 0:
#                 E = hata(x, y)
#                 print(f"{i}. iterasyon : x = {x} , y = {round(y,5)} , hata = {round(E,5)} ")
#                 x = x
#                 y = x_yeni
#
#
#             if denklem(y) < 0:
#                 E = hata(x, y)
#                 print(f"{i}. iterasyon : x = {x} , y = {round(y,5)} , hata = {round(E,5)} ")
#                 x = x_yeni
#                 y = y
#
#         if c < 0:
#             if denklem(x) > 0:
#                 E = hata(x, y)
#                 print(f"{i}. iterasyon : x = {x} , y = {round(y,5)} , hata = {round(E,5)} ")
#                 x = x
#                 y = x_yeni
#
#             if denklem(y) > 0:
#                 E = hata(x, y)
#                 print(f"{i}. iterasyon : x = {x} , y = {round(y,5)} , hata = {round(E,5)} ")
#                 x = x_yeni
#                 y = y
#
#     elif (a*b)>0:
#         print("kök tanımlı değil")
#     else:
#         print(f"kök : {a} ve {b} 'dir.")
#



#filter map kullanımı
#
# def kare_al(sayi):
#     return sayi*sayi
#
#
# result = kare_al(5)
# print(result)
#
#
# # listedeki elemanları fonksiyonda kullanma map foonksiyonu ile
# liste = [1,2,3,4]
# list_result = list(map(kare_al,liste))
# print(list_result)
#
#
# for i in range(0, len(liste)):
#     print(kare_al(liste[i]))
#
#
# for i in map(kare_al,liste):
#     print(i)
#
#
# def kontrol(sayi):
#     return sayi%2==0
# sonuc = list(filter(kontrol,liste))
# print(sonuc)




#------------------------------------------------------------------------------------------------------------------------------------------
# #Bankamatik yapımı...
#
# onurHesap = {
#     'ad'  : "onur akın",
#     'hesapNo' : 321,
#     'bakiye' : 3000,
#     'ekHesap' : 2000
# }
#
# angelineHesap = {
#     'ad'  : "angelina joliie",
#     'hesapNo' : 123,
#     'bakiye' : 4000,
#     'ekHesap' : 5000
# }
#
# def paraCek(hesap,cekilecekMiktar):
#
#     if hangiHesap==hesap['hesapNo']:
#         if hesap['bakiye']>=cekilecekMiktar:
#             hesap['bakiye']-cekilecekMiktar
#         else:
#             print("bakiye yetersiz")
#             girdi = input("ek hesabı kullanmak istermisiniz (e/h) : ")
#
#             if girdi=='e':
#                 if hesap['bakiye']+hesap['ekHesap']>=cekilecekMiktar:
#                     hesap['ekHesap']=hesap['bakiye']+hesap['ekHesap'] - cekilecekMiktar
#                     hesap['bakiye'] = 0
#                     print(hesap['ekHesap'])
#                     print(hesap['bakiye'])
#             elif girdi == 'h':
#                 print("yetersiz bakiye çıkış yapılıyor ...")
#             else:
#                 print("yanlış girdi çıkış yapılıyor ...")
#
# print("--- BANKAMATİĞE HOŞGELDİNİZ ---")
# print("1-Para Çekme")
# print("2-Para Yatırma")
# print("3-Para Gonderme")
# deger = int(input("İşlemi Giriniz (1,2,3) : "))
#
# if deger==1 or deger==2 or deger==3 :
#     hangiHesap = int(input("hesap numarısını giriniz : "))
#
# if deger==1:
#     paraCek(onurHesap,2000)

# elif deger==2:
#
# elif deger==3:
#
# else :
#     print("yanlış değer girildi ")
#     print("sistemden çıkılıyor...")
#------------------------------------------------------------------------------------------------------------------------------------------



# a = "onur"
#
# b=dir(a)
# print(b)

#
# def dondur(a):
#     print(a*a*a)
#
# a = int(input("sayi gir : "))
# dondur(a)
#
