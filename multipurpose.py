import cv2

kamera = cv2.VideoCapture(0)

kamera.release()
cv2.destroyAllWindows()


kullanici_bilgileri = {
    "kullanici1": "1234",
    "kullanici2": "4567",
    "kullanici3": "7890",
}

print("""

 __       __            __    __      __                                                                                _______                                                                
/  \     /  |          /  |  /  |    /  |                                                                              /       \                                                               
$$  \   /$$ | __    __ $$ | _$$ |_   $$/   ______   __    __   ______    ______    ______    _______   ______          $$$$$$$  | ______    ______    ______    ______   ______   _____  ____  
$$$  \ /$$$ |/  |  /  |$$ |/ $$   |  /  | /      \ /  |  /  | /      \  /      \  /      \  /       | /      \  ______ $$ |__$$ |/      \  /      \  /      \  /      \ /      \ /     \/    \ 
$$$$  /$$$$ |$$ |  $$ |$$ |$$$$$$/   $$ |/$$$$$$  |$$ |  $$ |/$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$$/ /$$$$$$  |/      |$$    $$//$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$  |$$$$$$ $$$$  |
$$ $$ $$/$$ |$$ |  $$ |$$ |  $$ | __ $$ |$$ |  $$ |$$ |  $$ |$$ |  $$/ $$ |  $$ |$$ |  $$ |$$      \ $$    $$ |$$$$$$/ $$$$$$$/ $$ |  $$/ $$ |  $$ |$$ |  $$ |$$ |  $$/ /    $$ |$$ | $$ | $$ |
$$ |$$$/ $$ |$$ \__$$ |$$ |  $$ |/  |$$ |$$ |__$$ |$$ \__$$ |$$ |      $$ |__$$ |$$ \__$$ | $$$$$$  |$$$$$$$$/         $$ |     $$ |      $$ \__$$ |$$ \__$$ |$$ |     /$$$$$$$ |$$ | $$ | $$ |
$$ | $/  $$ |$$    $$/ $$ |  $$  $$/ $$ |$$    $$/ $$    $$/ $$ |      $$    $$/ $$    $$/ /     $$/ $$       |        $$ |     $$ |      $$    $$/ $$    $$ |$$ |     $$    $$ |$$ | $$ | $$ |
$$/      $$/  $$$$$$/  $$/    $$$$/  $$/ $$$$$$$/   $$$$$$/  $$/       $$$$$$$/   $$$$$$/  $$$$$$$/   $$$$$$$/         $$/      $$/        $$$$$$/   $$$$$$$ |$$/       $$$$$$$/ $$/  $$/  $$/ 
                                         $$ |                          $$ |                                                                         /  \__$$ |                                 
                                         $$ |                          $$ |                                                                         $$    $$/                                  
                                         $$/                           $$/                                                                           $$$$$$/                                   
Made Wolfho :) """)

def kullanici_girisi(kullanici_ad, sifre):
    if kullanici_ad in kullanici_bilgileri and kullanici_bilgileri[kullanici_ad] == sifre:
        return True
    else:
        return False


kullanici_ad = input("Kullanıcı adınızı girin: ")
sifre = input("Şifrenizi girin (Sadece sayılar): ")

if kullanici_girisi(kullanici_ad, sifre):
    print("Giriş başarılı!")

    while True:
        print("Ne yapmak istiyorsunuz?")
        print("""
              1. Kullanıcı Bilgileri
              2. Python'da yaptığım projeler
              3. Kamera Programını Çalıştır
              4. Not Defteri
              5. Çıkış """)
        secim = input("Yapmak istediğiniz işlemi seçin (1-5): ")

        if secim == "1":
            print(kullanici_bilgileri)
        elif secim == "2":
            print("""
            1. Atm Programı Projesi (python)
            2. Web Scraper Projesi (python)""")
        elif secim == "3":
            print("Kamera Açılıyor...(Çıkmak için 'x' tuşuna basınız)")
            kamera = cv2.VideoCapture(0)
            while True:
                ret, videoGoruntu = kamera.read()

                cv2.imshow("Kamera", videoGoruntu)

                if cv2.waitKey(50) & 0xFF == ord('x'):
                    break

            kamera.release()
            cv2.destroyAllWindows()
        elif secim == "4":
            def not_defteri():
                notlar = {}

                def not_ekle():
                    baslik = input("Not başlığı: ")
                    icerik = input("Not içeriği: ")
                    notlar[baslik] = icerik
                    print("Not başarıyla eklendi!")

                def not_goruntule():
                    if not notlar:
                        print("Not defteriniz boş.")
                    else:
                        print("Notlarınız:")
                        for baslik, icerik in notlar.items():
                            print(f"\n{baslik}:\n{icerik}")

                def not_sil():
                    if not notlar:
                        print("Not defteriniz boş. Silecek not yok.")
                    else:
                        baslik = input("Silmek istediğiniz not başlığı: ")
                        if baslik in notlar:
                            del notlar[baslik]
                            print(f"'{baslik}' başlıklı not silindi.")
                        else:
                            print(f"'{baslik}' başlıklı not bulunamadı.")

                def menu_goster():
                    print("\nNOT DEFTERİ")
                    print("1. Not Ekle")
                    print("2. Notları Görüntüle")
                    print("3. Not Sil")
                    print("4. Not Defteri Menüsünden Çık")

                while True:
                    menu_goster()
                    secim = input("Seçiminizi yapın (1-4): ")

                    if secim == "1":
                        not_ekle()
                    elif secim == "2":
                        not_goruntule()
                    elif secim == "3":
                        not_sil()
                    elif secim == "4":
                        print("Not defteri menüsünden çıkılıyor...")
                        break
                    else:
                        print("Geçersiz seçim. Lütfen tekrar deneyin.")

            not_defteri()
        elif secim == "5":
            print("Programdan çıkılıyor....")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
else:
    print("Kullanıcı adı veya şifre yanlış.")