import time
class Encryption():
    def __init__(self):
        pass      

    def Sifrele(self):
        while True:
                time.sleep(1)
                print("Bir mesaj ve bir kriptolama sayısı giriniz.")
                mesaj1=input("Mesaj:")
                mesaj1=mesaj1.lower()
                mesaj1=mesaj1.replace(" ","")
                if not mesaj1.isalpha():
                    print("Lütfen doğru bir kelime giriniz.")
                    continue
                try:
                    sayi1=int(input("Kriptolama Sayısı:"))
                except ValueError:
                    print("Lütfen bir sayı giriniz.")
                    continue
                for i in mesaj1:
                    #Girilen sayının ASCII değerini alıp ona göre işlemler yapar.
                    kriptosayi = ord(i) + sayi1
                    if(kriptosayi>122):
                        kriptosayi2 = 96 + kriptosayi - 122
                        print(chr(kriptosayi2), end="")
                    else:
                        print(chr(kriptosayi), end="")
                break
        
    def SifreCöz(self):
        while True:
            time.sleep(1)
            print("Kriptolanmış mesaj ve bir çözücü sayı giriniz.")
            mesaj2=input("Kriptolanmış Mesaj:")
            mesaj2=mesaj2.lower()
            mesaj2=mesaj2.replace(" ","")
            try:
                sayi2=int(input("Çözücü Sayı:"))
            except ValueError:
                print("Lütfen bir sayı giriniz.")
                continue
            for i in mesaj2:
                #Girilen sayının ASCII değerini alıp ona göre işlemler yapar.
                cözücüsayi = ord(i) - sayi2
                if(cözücüsayi<97):
                    cözücüsayi2 = 122 + cözücüsayi - 96
                    print(chr(cözücüsayi2), end="")
                else:
                    print(chr(cözücüsayi), end="")
            break

    def Menü(self):
        while True:
            print("\nKriptolama Uygulamasına Hoşgeldiniz!\n"
                "------------------------------------\n"
                "Mesajı Kodlamak İçin = 1\n"
                "Mesajı Çözmek İçin = 2\n"
                "Projeden Çıkmak İçin = 3")
            secim = int(input("\nSeçiminiz:"))
            if (secim == 1):
                time.sleep(2)
                self.Sifrele()
            elif (secim == 2):
                time.sleep(2)
                self.SifreCöz()
            elif (secim == 3):
                print("Programdan çıkılıyor...")
                time.sleep(2)
                break
            else:
                print("Lütfen doğru seçim yapınız.")
sifre = Encryption()
sifre.Menü()
