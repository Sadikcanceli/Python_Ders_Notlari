for numbers in range(10): # range burada 0-9 arası bir sayı döngüsü oluşturur 
    print(numbers) #bu döngü için bir lite yapıp döngüye sokmama gerek kalmaz

index = 0
greeting = "Hello"

for letter in greeting:
    print(f"İndex: {index} Letter: {greeting[index]} ")
    index += 1
print("***************")
for letter in greeting:
    print(f"İndex: {index} Letter: {letter} ")
    index += 1
print("***************")
for index,letter in enumerate(greeting):
    print(f"index: {index} letter: {letter}")

for x in range(10):
    print(x) 

numbers = [x for x in range(10)] # ilk x döngüye giren ikinci x den gelen değerleri numbers içine atıyor 
print(numbers) # ikinci x ise döngüye girip 0 dan 9 a kadar olan sayıları döndürüyor 

   