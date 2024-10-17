
# name = input("enter a name : ")
# print("Hello",name)

# s1 = int(input("a:"))
# s2 = int(input("b:"))
# print(s1+s2)

# s1 = int(input("a:"))
# s2 = int(input("b:"))
# total = (s1+s2)/2
#
# if total<50:
#     print("you stayed")
# else:
#     print("you passed")

# for i in range(1,101):
#     print(i)

# for i in range(2,101,2):
#     print(i)

# for i in range(1,101):
#     if i%5==0 and i%3==0:
#         print(i)

# x = 1
# a = int(input("enter a number : "))
# control = True
#
# if a>x: #pozitif
#     control=True
# elif x>a: #negatif
#     control=False
#
# if control==True:
#     for i in range(1,a+1):
#         print(i)
# elif control==False:
#     for i in range(a,2,1):
#         print(i)

# word = input("enter a word : ")
# for i in range(len(word)):
#     print(word[i])

# control = True
# s1 = int(input("enter a number : "))
# s2 = int(input("enter a number : "))
#
# if s1 > s2:
#     control = True
# elif s2 > s1:
#     control = False
# else:
#     print("esit")
#
# if control== True:
#     for i in range(s1,s2-1,-1):
#         print(i)
# elif control==False:
#     for i in range(s1,s2+1):
#         print(i)

# total = 0
# s1 = int(input("s1 : "))
# s2 = int(input("s1 : "))
#
# for i in range(s1,s2+1):
#     total += i
# print(total)

# a = int(input("a "))
#
# if a == 2:
#     print("asal")
#
# for i in range(2,a):
#     if a%i==0:
#         print("asal değil")
#         break
# else:
#     print("asal")

# sayi = 5
# hak = 3
#
# while True:
#     print("hak : ", hak)
#     a = int(input("enter a number : "))
#     if a==sayi:
#         print("dogru bildiniz")
#         break
#     if hak==1:
#         print("hak bitti sayi :",sayi)
#         break
#     elif a>sayi:
#         hak=hak-1
#         print("yablış tahmin aşağı in ")
#     elif sayi>a:
#         hak=hak-1
#         print("yanlış girdiniz yukarı çık ")

# liste = [1,2,5,10,15,17,22]
#
# for i in range(len(liste)):
#     if liste[i]%5==0:
#         print(liste[i])

# harf = "e"
# word = "fdafnkaewqeöqwdm"
#
# for i in range(len(word)):
#     if word[i] in harf:
#         print(f"{i}. da var")

# liste = [3,1,2]
# print(liste)
# liste[0] = 1
# print(liste)

# hg = ["pzt","sa","car","per","cum"]
# for i in hg:
#     if "per" and "cum" in hg:
#         print("var")
#         break
#     else:
#         print("yok")
#         break


# sayi = input("sayi gir : ")
# toplam = 0
#
# for i in sayi:
#     toplam += int(i)
# print(toplam)



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#x = [2000,1000,500] max havuzun büyüklüğü
# her eksen baiına -3 ile 3 arasında bir yer değişim olacak
# her harekette -1 ile 1 arasında sapma olacak

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



# toplam = 0
# sayi = input("sayi gir : ")
#
# for i in range(len(sayi)):
#     toplam += int(sayi[i])
# print(toplam)


# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} x {j} = ",i*j ,end=" , ")
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if i<=j:
#             print(j,end="")
#     print()



#For örnekleri:


# for i in range(4):
#     for j in range(4):
#         print("*",end="")
#     print()


# for i in range(1,6):
#     for j in range(1,i+1):
#             print("*",end="")
#     print()


# for i in range(5,0,-1):
#     print("*"*i)


# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# for i in range(5,1,-1):
#     for j in range(1,i):
#         print("*",end="")
#     print()


# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(" ",end="")
#     for k in range(2*j-1):
#         print(i*"*",end="")
#     print()
#




