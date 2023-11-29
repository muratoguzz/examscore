def notGir():
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    not1 = input("1. notu gir: ")
    not2 = input("2. notu gir: ")
    not3 = input("3. notu gir: ")
    
    with open("sinavNotlari.txt", "a", encoding= "utf-8") as file:
        file.write(ad+" "+soyad+":"+" "+not1+","+not2+","+not3+"\n")  
           
def notHesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    adSoyad = liste[0]
    notlar = liste[1].split(",")
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    
    ortalama = (not1+not2+not3)/3
    
    if ortalama>=90 and ortalama<=100:
        harf = "AA"
    elif ortalama>=85 and ortalama<=89:
        harf = "BA"
    elif ortalama>=80 and ortalama<=84:
        harf = "BB"
    elif ortalama>=75 and ortalama<=79:
        harf = "CB"
    elif ortalama>=70 and ortalama<=74:
        harf = "CC"
    elif ortalama>=65 and ortalama<=69:
        harf = "DC"
    elif ortalama>=60 and ortalama<=64:
        harf = "DD"
    elif ortalama>=50 and ortalama<=59:
        harf = "FD"
    else:
        harf = "FF"
    return adSoyad+":"+harf+"\n"

def notlariOku():
    with open("sinavNotlari.txt", "r", encoding= "utf-8") as file:
        for i in file:
            print(notHesapla(i))
            
def notlariKaydet():
    with open("sinavNotlari.txt", "r", encoding= "utf-8") as file:
        liste = []
        for i in file:
            liste.append(notHesapla(i))
            
        with open("sonuclar.txt", "a", encoding= "utf-8") as file2:
            for i in liste:
                file2.write(i)
                
while True:
    x = input("1-Notları oku\n2-Not gir\n3-Notları kaydet\n4-Çıkış\n")
    if x=="1":
        notlariOku()
    elif x=="2":
        notGir()
    elif x=="3":
        notlariKaydet()
    else:
        break