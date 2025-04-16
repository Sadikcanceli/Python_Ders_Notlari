x=5
y=25

x=y
#burada xi 25 yaparız sonradan y ynin değerini değiştirirsek x değişmez
y=10
print(x)
print(y)

a=["apple","banana"]
b=["apple","banana"]
# burada a ya byi atadık sonra b değişince a da değişti
#bunun sebebi liste tipindeki veri tipleri referans tiptir yani lste tipindeki veri tipleri bellekte bir adres tutarlar
#bu sayede a=b dediğiimizde a nın adresi b nin adresine eşitlenir
#bu yüzden b değişince a da değişir

a=b
b[0]="grape"
print(a,b)