try:
        number = int(input("Lütfen 1 ile 100 arasında bir sayı girin: "))#kullanıcıdan sayı alınıyor
        if number <= 100 and number >= 1:# 1-100 arasında sayı girilirse döngüden çıkacak
            break
            print("Lütfen 1 ile 100 arasında bir sayı girin: ") # 1-100 dışında sayı girilirse hata yakalanır
    except ValueError: # geçersiz bir değer girildiğinde hata yakalanır
        print("Geçerli bir sayı girin!")