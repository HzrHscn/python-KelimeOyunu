import random
from unidecode import unidecode

def kelime_oyunu():
    puan = 10

    def tahmin_hakkı(kelime):
        nonlocal puan
        tahminler = 3
        harf_sayısı = len(kelime)
        gizli_kelime = '_' * harf_sayısı

        while tahminler > 0:
            print("Tahmin hakkınız:", tahminler)
            print("Gizli kelime:", gizli_kelime)
            tahmin = input("Bir harf tahmin edin veya kelimeyi tamamlayın: ").lower()

            if tahmin == kelime:
                return True

            if tahmin in kelime:
                gizli_kelime = gizli_kelime_olustur(tahmin, kelime, gizli_kelime)
                print("Doğru tahmin! +2 puan kazandınız.")
                puan += 2
                if gizli_kelime == kelime:
                    return True
            else:
                tahminler -= 1
                print("Yanlış tahmin! -1 puan.")
                puan -= 1

        return False

    def gizli_kelime_olustur(tahmin, kelime, gizli_kelime):
        yeni_gizli_kelime = ""
        for i in range(len(kelime)):
            if tahmin == kelime[i]:
                yeni_gizli_kelime += tahmin
            else:
                yeni_gizli_kelime += gizli_kelime[i]
        return yeni_gizli_kelime

    def soruları_oku(dosya_adı):
        sorular = []
        cevaplar = []
        with open(dosya_adı, 'r', encoding='utf-8') as dosya:
            satırlar = dosya.readlines()
            for i, satır in enumerate(satırlar):
                if i % 2 == 0:
                    sorular.append(satır.strip())
                else:
                    cevaplar.append(satır.strip())
        return sorular, cevaplar

    sorular, cevaplar = soruları_oku("sorular.txt")

    for i in range(len(sorular)):
        print("Puanınız:", puan)
        print("Soru:", sorular[i])
        cevap = unidecode(cevaplar[i].lower())

        if tahmin_hakkı(cevap):
            print("Doğru cevap! +2 puan kazandınız.")
            puan += 2
        else:
            print("Yanlış cevap! Doğru cevap:", cevap)
            puan -= 1

        if puan <= 0:
            print("Oyunu kaybettiniz.")
            break
        elif puan >= 20:
            print("Tebrikler! Kazandınız.")
            break

kelime_oyunu()
