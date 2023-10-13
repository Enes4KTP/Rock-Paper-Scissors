import random

kullanicipuan = 0
bilgisayarpuan = 0

while kullanicipuan < 10 and bilgisayarpuan < 10:
    print('\n')
    print("1 - Taş")
    print("2 - Kağıt")
    print("3 - Makas")
    print("4 - Kertenkele")
    print("5 - Spock")

    secim = input("Seçiminizi yapınız.\n")
    print('\n')

    if secim == "1":
        secim = 'Taş'
    elif secim == "2":
        secim = 'Kağıt'
    elif secim == "3":
        secim = 'Makas'
    elif secim == "4":
        secim = 'Kertenkele'
    elif secim == "5":
        secim = 'Spock'
    else:
        print("Yanlış seçim yaptınız. Lütfen 1-5 arasında bir seçim yapınız.")
       
    list = ['Taş', 'Kağıt', 'Makas', 'Kertenkele', 'Spock']
    randomSecim= random.choice(list)
    
    if randomSecim == 'Kağıt':
        if secim == 'Taş':
            bilgisayarpuan += 1
            print(secim)
            print(randomSecim)
            print("Kaybettiniz. Bilgisayarın puanı: ", bilgisayarpuan)
        elif secim == 'Kağıt':
            print(secim)
            print(randomSecim)
            print("Berabere!")
        elif secim == 'Makas':
            kullanicipuan += 1
            print(secim)
            print(randomSecim)
            print("Tebrikler! Kazandınız. Puanınız:", kullanicipuan)
        elif secim == 'Kertenkele':
            kullanicipuan += 1
            print(secim)
            print(randomSecim)
            print("Tebrikler! Kazandınız. Puanınız:", kullanicipuan)
        elif secim == 'Spock':
            bilgisayarpuan += 1
            print(secim)
            print(randomSecim)
            print("Kaybettiniz. Bilgisayarın puanı: ", bilgisayarpuan)
    
    if randomSecim == 'Taş':
        if secim == 'Kağıt':
            kullanicipuan += 1
            print(secim)
            print(randomSecim)
            print("Tebrikler! Kazandınız. Puanınız:", kullanicipuan)
        elif secim == 'Taş':
            print(secim)
            print(randomSecim)
            print("Berabere!")
        elif secim == 'Makas':
            bilgisayarpuan += 1
            print(secim)
            print(randomSecim)
            print("Kaybettiniz. Bilgisayarın puanı: ", bilgisayarpuan)
        elif secim == 'Kertenkele':
            bilgisayarpuan += 1
            print(secim)
            print(randomSecim)
            print("Kaybettiniz. Bilgisayarın puanı: ", bilgisayarpuan)
        elif secim == 'Spock':
            kullanicipuan += 1
            print(secim)
            print(randomSecim)
            print("Tebrikler! Kazandınız. Puanınız:", kullanicipuan)
    
    if randomSecim == 'Makas':
        if secim == 'Kağıt':
            bilgisayarpuan += 1
            print(secim)
            print(randomSecim)
            print("Kaybettiniz. Bilgisayarın puanı: ", bilgisayarpuan)
        elif secim == 'Makas':
            print(secim)
            print(randomSecim)
            print("Berabere!")
        elif secim == 'Taş':
            kullanicipuan += 1
            print(secim)
            print(randomSecim)
            print("Tebrikler! Kazandınız. Puanınız:", kullanicipuan)
        elif secim == 'Kertenkele':
            bilgisayarpuan += 1
            print(secim)
            print(randomSecim)
            print("Kaybettiniz. Bilgisayarın puanı: ", bilgisayarpuan)
        elif secim == 'Spock':
            kullanicipuan += 1
            print(secim)
            print(randomSecim)
            print("Tebrikler! Kazandınız. Puanınız:", kullanicipuan)
            
    if randomSecim == 'Kertenkele':
         if secim == 'Kağıt':
             bilgisayarpuan += 1
             print(secim)
             print(randomSecim)
             print("Kaybettiniz. Bilgisayarın puanı: ", bilgisayarpuan)
         elif secim == 'Kertenkele':
             print(secim)
             print(randomSecim)
             print("Berabere!")
         elif secim == 'Taş':
             kullanicipuan += 1
             print(secim)
             print(randomSecim)
             print("Tebrikler! Kazandınız. Puanınız:", kullanicipuan)
         elif secim == 'Makas':
             kullanicipuan += 1
             print(secim)
             print(randomSecim)
             print("Tebrikler! Kazandınız. Puanınız:", kullanicipuan)
         elif secim == 'Spock':
             bilgisayarpuan += 1
             print(secim)
             print(randomSecim)
             print("Kaybettiniz. Bilgisayarın puanı: ", bilgisayarpuan)
             
    if randomSecim == 'Spock':
         if secim == 'Kağıt':
             kullanicipuan += 1
             print(secim)
             print(randomSecim)
             print("Tebrikler! Kazandınız. Puanınız:", kullanicipuan)
         elif secim == 'Spock':
             print(secim)
             print(randomSecim)
             print("Berabere!")
         elif secim == 'Taş':
             bilgisayarpuan += 1
             print(secim)
             print(randomSecim)
             print("Kaybettiniz. Bilgisayarın puanı: ", bilgisayarpuan)
         elif secim == 'Makas':
             bilgisayarpuan += 1
             print(secim)
             print(randomSecim)
             print("Kaybettiniz. Bilgisayarın puanı: ", bilgisayarpuan)
         elif secim == 'Kertenkele':
             kullanicipuan += 1
             print(secim)
             print(randomSecim)
             print("Tebrikler! Kazandınız. Puanınız:", kullanicipuan)
             
print("Oyun Sona Erdi")
print('\n')

if bilgisayarpuan == 10:
    print("Oyunu Kaybettiniz. Bilgisayar Kazandı.")
elif kullanicipuan == 10:
    print("Siz Kazandınız. Tebrikler!")