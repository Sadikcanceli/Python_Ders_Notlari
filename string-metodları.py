message = "Hello, My name is Sadikcan Çelik\n"
print(message)
message = message.upper() #hepsini büyük yapar
print(message)
message = message.lower() #hepsini küçük yapar 
print(message)
message = message.title() #baş harfleri büyük yapar 
print(message)
message = message.capitalize() #sadece ilk harf büyük oldu 
print(message)
message = message.strip() #başta boşluk varsa onu giderir
print(message)
message = message.split() # her boşlu arasındaki kelimeleri ayırır
print(message)
message = '* *'.join(message)# ayrılan stringleri birleştirir tırnak içine ne yazarsan ona göre birleşir 
print(message)
index = message.find("is")# sadıkcan kelimesini arar ve ilk harfin olduğu indexi döndürür 
print(index)
