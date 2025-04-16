list = [1,2,3,4,"salam"]

tuple = (1,6,3,"a")

print(type(list))
print(type(tuple))

list1=["ali","ahmet"]
tuple1=("veli","mehmet")
""" list1 ve tuple1 i tanımladık aşağıda list1'in 0. indisini sadık olarak değiştirebiliyorum ama tuple böyle bir şey yok """
print(list1 , "\n")
print(tuple1, "\n")
list1[0] = "sadık"        
print(list1 ,"\n")  

plakalar = {
                "istanbul":{"plaka":34,"nüfüs":"15m"},
                "ankara":6,
                "izmir":35
            } #key ve value değerlerini eşleştiriyoruz key değeri verince value değerine ulaşabiliyoruz

print(plakalar["istanbul"]["nüfüs"]) #istanbula alt keyler verdik
print(plakalar["istanbul"]["plaka"])
print(plakalar["izmir"])
print(plakalar["ankara"])