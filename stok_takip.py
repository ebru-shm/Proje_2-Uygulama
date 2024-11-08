

def urun_ekle():
    
        dosya= open("C:/Users/user/Desktop/Python/vektorel/haf_05_02/urun.txt","a", encoding = "utf8")
        print("\n\n Ürün bilgilerini giriniz: ")
        urun_adi = input("Ürün adı: ")
        urun_kodu = input("Ürün kodu: ")
        stok_miktari = int(input("Stoktaki miktar: "))
        stok_guncelleme_tarihi = input("Stok güncelleme tarihi: ")
        dosya.write(f"{urun_adi}#{urun_kodu}#{stok_miktari}#{stok_guncelleme_tarihi}\n")
        dosya.close()

        secim = input("Başka ürün eklemek ister misiniz?(E/H) ").lower()

        if secim == "e":
            urun_ekle()
        else:
            print("\n\nStoktakiler (yeni şekli):")
            stok_listele()
            anamenu()



def stok_listele():
  
        print("\n\nStok Listesi: ")
        dosya = open("C:/Users/user/Desktop/Python/vektorel/haf_05_02/urun.txt",encoding = "utf8")
        okunan = dosya.readlines()
        for sira,a in enumerate(okunan):
            b = a.split("#")
            print(f"{sira+1} - {b[0]},\t Ürün kodu: {b[1]},\t Stok miktarı: {b[2]},\t Stok güncellenme tarihi: {b[3]}")
        dosya.close()
   

def urun_sil(): 

    urun_kodu = input("Stok listesinden çıkarmak istediğiniz ürünün kodunu giriniz: ")
    dosya = open("C:/Users/user/Desktop/Python/vektorel/haf_05_02/urun.txt","a+")
    dosya.seek(0)
    satirlar=dosya.readlines()
    stok_list=[]
    stok_list_yeni = [] 
    for satir in satirlar:
        kod = satir.split("#")
        stok_list.append(kod)
    for kod in stok_list:
        if kod[1] == urun_kodu:
            print("Ürün listeden silindi.")
        else:
            stok_list_yeni.append(kod)
    dosya.close() 
   

 
# 
#     print("Mevcut Kayıtlar")
#     # rehber_listele()
#     silinecek= input("Hangi kayıt silinecek(numarasını girin): ")
#     dosya = open("rehber.txt","r")
#     okunan = dosya.readlines()
#     print(okunan)
#     for s, a in enumerate(okunan):
#         print(s,a)
#         if s!= silinecek: dosya.write(a)
#     dosya.close()

    # dosya.close()
    # dosya = open("rehber.txt","w")

    # for sira,a in enumerate(okunan):
    #     if sira!= silinecek: dosya.write(a)
    
    # dosya.close()


# def urun_düzenle(): 
#     pass

# def urun_ekle(): 
#     pass

def anamenu():
    
    #print("╔"+"═"*20+"╗")
    print("╔═══════════════════════╗")
    print("║ STOK TAKİP UYGULAMASI ║")
    print("║                       ║")
    print("║  1-Ürün ekle          ║")
    print("║  2-Stok listesi       ║")
    print("║  3-Ürün Düzenle       ║")
    print("║  4-Ürün Silme         ║")
    print("║  5-Çıkış              ║")
    print("║                       ║")
    print("║  Seçimiz nedir?       ║")
    print("╚═══════════════════════╝")
    # 201 ╔ 187 ╗ 200 ╚  # 188 ╝

    secim = input ("Seçiminiz: ")
    
    if secim =="1": urun_ekle(); anamenu()
    elif secim =="2": stok_listele(); anamenu()
    elif secim =="3": urun_sil(); anamenu()
    elif secim =="4": urun_düzenle(); anamenu()
    elif secim =="5": urun_ekle(); anamenu()
        
        
anamenu()


