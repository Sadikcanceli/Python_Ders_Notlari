name = "Sadıkcan Çelik"

for letter in name:
    if letter == "Ç":   
        break #break ifadesi döngüyü kırar ve Ç harfine geldikten sonra döngüden çıkar
    print(letter)

for letter in name:
    if letter == "k":
        continue #continue ifadesinde letter = k olduğunda döngünün o sefer çalışmasını atlar ve k yı yazdırmaz
    print(letter)