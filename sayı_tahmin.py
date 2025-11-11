import random

doğru_sayı = random.randint(0, 101)
tahmin_sayısı=0

while tahmin_sayısı<5:      #for i in range(101)  çalışırdı ama gereksiz 101 kere döngü kurmaya gerek yok
    kullanıcı_sayısı=int(input("tahmininiz nedir:"))
    if kullanıcı_sayısı==doğru_sayı:
        print("tebrikler doğru tahmin\noyun sonlandı")
        break
    elif kullanıcı_sayısı<doğru_sayı:
        print("daha yüksek bir rakam giriniz")
    else:
        print("daha düşük bir rakam giriniz")
    tahmin_sayısı+=1
    if tahmin_sayısı==5:
        print(f"tahmin sayınız doldu. doğru tahmin:{doğru_sayı}")


