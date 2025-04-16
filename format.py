name="Sadikcan"
surname="Celik"
age=19

print("My name is {} {}".format(name,surname))
print("My name is {s} {n}".format(n=name,s=surname))#normalde sıra önemli ben burda ters yaptım
print("My name is {} {} and I'm {} years old".format(name,surname,age))
print(f"My name is {name} {surname} and I'm {age} years old")#daha kısa bir yol 

result=200/700

print("the result is:{}".format(result))#çok fazla basamak var 
print("the result is:{:.3f}".format(result))#virgülden önceki ilk basamak ve virgülden sonraki 3 basamağı al dedim

