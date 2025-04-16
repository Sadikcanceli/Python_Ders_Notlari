numbers = [1, 2, 3, 4, 5]

for num in numbers: #basit bir for döngüsü örneği pythonda c gibi kaç kere çalışacağını ayarlamaya gerek yok
    print(num) #pyhton da döngü burada num değişkeni foreach yani her biri nin karşılığı 
    #burada num numbers içindeki 10 elemanın her biri için döngüyü bir kere çalıştırır

    d = { "k1": 1, "k2": 2, "k3": 3 }

for key in d:
    print(key) #bu şekilde sadece keyleri alırız
for key,value in d.items():    
    print(key,value) #bu şekilde key ve value yi birlikte alırız

x = 0 #basit bir while döngüsü örneği
while x <= 5:
    print(x)
    x+=1

name = '' #false
while not name.strip():
    name = input("Enter your name: ")

print(f"Hello, {name}")

    