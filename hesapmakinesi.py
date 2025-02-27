def hesap_makinesi():
    print("Hesap Makinesi\n1: Toplama\n2: Çıkarma\n3: Çarpma\n4: Bölme")
    secim = input("Bir işlem seçin (1/2/3/4): ")

    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

    if secim == '1':
        print("Sonuç:", sayi1 + sayi2)
    elif secim == '2':
        print("Sonuç:", sayi1 - sayi2)
    elif secim == '3':
        print("Sonuç:", sayi1 * sayi2)
    elif secim == '4':
        if sayi2 != 0:
            print("Sonuç:", sayi1 / sayi2)
        else:
            print("Hata: Sıfıra bölme hatası!")
    else:
        print("Geçersiz giriş!")

while True:
    hesap_makinesi()