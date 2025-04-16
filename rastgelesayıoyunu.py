# Rastgele sayı oyunu

#zorluk seçeneği ekle ve her zorluk seviyesinde farklı sayıda tahmin hakkı ver

import random # Rastgele sayı oluşturmak için random modülünü içe aktar

random_number = random.randint(1, 100) # rastgele sayı oluşturluyor

while True: #kullanıcı 1-100 arasında sayı girene kadar devam edecek döngü
    try:
        number = int(input("Lütfen 1 ile 100 arasında bir sayı girin: "))#kullanıcıdan sayı alınıyor
        if number <= 100 and number >= 1:# 1-100 arasında sayı girilirse döngüden çıkacak
            break
            print("Lütfen 1 ile 100 arasında bir sayı girin: ") # 1-100 dışında sayı girilirse hata yakalanır
    except ValueError: # geçersiz bir değer girildiğinde hata yakalanır
        print("Geçerli bir sayı girin!")

hak = 5 # Kullanıcının tahmin hakkı

while number != random_number and hak != 0:# kullanıcı doğru tahmin edene veya hakları bitene kadar döngü devam edecek
    hak -= 1
    print(f"Kalan hak: {hak}")
    if hak == 0: # Kullanıcının hakkı kalmadığında döngüden çıkacak
        break
    if number < random_number: # Kullanıcının girdiği sayı rastgele sayıdan küçükse gelen mesaj
        print("Daha büyük bir sayı girin.")
        number = int(input("Lütfen 1 ile 100 arasında bir sayı girin: "))
    else:
        print("Daha küçük bir sayı girin.") # Kullanıcının girdiği sayı rastgele sayıdan büyükse gelen mesaj
        number = int(input("Lütfen 1 ile 100 arasında bir sayı girin: "))

if number == random_number: # Kullanıcı doğru tahmin ettiğinde gelen mesaj
    print(f"Tebrikler! Doğru tahmin ettiniz. Sayı: {random_number}")
else: # Kullanıcı hakkı kalmadığında gelen mesaj
    print("Haklarınız kalmadı. Oyun bitti.")
