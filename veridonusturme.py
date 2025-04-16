x = input("1.sayi")
y = input("2.sayi")

toplam = int(x)+int(y) 
"""
eğer int() yapip bunlari int tipine çevirmezsem x ve y ye 
girilen değerleri string olarak algilar ve mesela 10 20 girildiyse 1020 şeklinde çikti verir 
ama bunlari int tipine çevirirsem sayi olarak alip toplar
"""
print(toplam)
# veri tipi dönüştürmek için veriyi yukarıdaki gibi istenilen veri tipi içine almalıyız
#int için int()
#float için float()
#string için str()
# bool için bool() 0 için false diğer her değer için true olur
"""
her veri tipi her veri tipine dönmez desteklenenler 

int -> float
float -> int
int -> bool ve float -> bool 0 için false diğer her değer için true olur
int, float, bool -> str
str -> bool (" " -> False, diğer tüm stringler -> True)
list, tuple, set, dict -> bool (Boş koleksiyonlar False, dolular True)
str -> int veya str -> float (Eğer string sadece rakamlardan oluşuyorsa)
"""