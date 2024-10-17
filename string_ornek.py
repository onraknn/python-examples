print("#------------------ 1 MİLYON İSTİHDHAM ÖRNEKLERİ -----------------------------")


website = "http://www.sadikturan.com"
course = "Python kursu: Baştan sona Python programlama rehberiniz (40 saat)"

"""
print(len(course)) # 65
print(website[7:]) # www.sadikturan.com
print(website[-3:])


a =course[15:] # ilk 15 ve son 15 karakter.
print(a[:15])

print(course[::-1]) # sondan başa sıralama
print("\n")

print("#----------------------------------------------------------------------------")

"""
"""
name,surname,age,job = "onur","akın",21,"student"

print(f"My name is {name} {surname}, i am {age} years old  my profession is a {job}")
print("\n")
print("#----------------------------------------------------------------------------")


a = "hello world"
b=a.replace('w','W')
print(b)
print("\n")
"""
print("#----------------------------------------------------------------------------")
"""
a="123"
print(a*3)
print("\n")

print("#----------------------------------------------------------------------------")
"""
"""
message = " denemeye hoşgeldiniz nasılsınız efendim iyimisiniz"

print(message.title()) # basları büyük yapar
print(message.capitalize()) # en baştakini büyültür.
print(message.strip()) # en başta boşluk varsa siler

message = message.split()
print(message[0])

print(message) # boşluktan sonra dizi içerisine alır.
message = '*'.join(message) # boşluklara * işareti kot splt ile çalıştı
print(message)

message = message.find('efendim')
print(message)

print("#----------------------------------------------------------------------------")

"""
website = website.count('a')
print(website)