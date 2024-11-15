def stok_ekle(): 
    dosya = open("stok_listesi.txt","a")
    print("\n\n Stok bilgilerini giriniz:")
    stok_kodu = input("Stok kodu: ")
    stok_adi = input("Stok adı: ")
    stok_miktari = int(input("Stok miktarı: "))
    stok_tarihi = input("Stok güncellenme tarihi: ")
    dosya.write(f"{stok_kodu}#{stok_adi}#{stok_miktari}#{stok_tarihi}\n")
    dosya.close()
    print("\n\nYeni Stok Listesi:")
    stok_listele()

def stok_listele(): 
    print("\n\nStok Listesi:")
    try:
        dosya = open("stok_listesi.txt")
    except:
        print("Dosya bulunamadı.")
        input()
    okunan = dosya.readlines()
    for sira,a in enumerate(okunan):
        b = a.split("#")
        print(f"{sira+1} - {b[0]},\t Stok adı: {b[1]},\t Stok miktarı: {b[2]},\t Stok güncellenme tarihi: {b[3]}")
    dosya.close()

def stok_duzelt(): 
    print("Mevcut stoklar")
    stok_listele()
    duzeltilecek = int(input ("Düzeltilecek olan stok kaydı(numarasını giriniz):"))
    dosya = open("stok_listesi.txt","r+")    
    okunan = dosya.readlines()
    duzeltilecekKayit = okunan[duzeltilecek-1]
    print("Düzeltilecek kayıt : ", duzeltilecekKayit)
    dosya.close()

    dosya = open("stok_listesi.txt","w")    
    for a in okunan:
        if a == duzeltilecekKayit: 
            print("\n\n Yeni bilgileri giriniz:")
            stok_kodu = input("Stok kodu: ")
            stok_adi = input("Stok adı: ")
            stok_miktari = int(input("Stok miktarı: "))
            stok_tarihi = input("Stok güncellenme tarihi: ")
            dosya.write(f"{stok_kodu}#{stok_adi}#{stok_miktari}#{stok_tarihi}\n")
        else: dosya.write(a)

    dosya.close()

def stok_sil(): 
    print("Mevcut stoklar")
    stok_listele()
    silinecek = int(input ("Hangi stok kaydını silmek istiyorsunuz?(numarasını giriniz):"))
    dosya = open("stok_listesi.txt","r+")    
    okunan = dosya.readlines()
    silinecekKayit = okunan[silinecek-1]
    print("Silinecek kayıt : ", silinecekKayit)
    dosya.close()

    dosya = open("stok_listesi.txt","w")    
    for a in okunan:
        if a != silinecekKayit: dosya.write(a)

    dosya.close()

def anamenu():
    # 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚ # 188 ╝
    print("╔═══════════════════════╗") # ╠ ╬ 
    print("║ STOK TAKİP UYGULAMASI ║")    
    print("║                       ║ ")
    print("║ 1-Stok ekle           ║")
    print("║ 2-Stok listesi        ║")
    print("║ 3-Stok düzenle        ║")
    print("║ 4-Stok silme          ║")
    print("║ 5-Çıkış               ║")
    print("║ Seçiminiz nedir?      ║")
    print("╚═══════════════════════╝")
    secim = input("Yapmak istediğiniz işlem: ")
    if secim == "1" : stok_ekle(); anamenu()   
    if secim == "2" : stok_listele(); anamenu()
    if secim == "3" : stok_duzelt(); anamenu()
    if secim == "4" : stok_sil(); anamenu()
    if secim == "5" : print("Sistemden çıkış yapılıyor."); exit()
    
anamenu()