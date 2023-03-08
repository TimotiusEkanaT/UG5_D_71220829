masuikk = input("masukkan asal mobil (ketik ""done"" untuk keluar)").lower()

jumlahSol = 0
jumlahSur = 0
jumlahJog = 0
jumlahMag = 0
def hitung_mobil(masuikk):
    while masuikk == True:
        if masuikk == "solo":
            jumlahSol + 1
            masuikk = input("masukkan asal mobil (ketik ""done"" untuk keluar)").lower()

        elif masuikk == "surabaya":
            jumlahSur + 1
            masuikk = input("masukkan asal mobil (ketik ""done"" untuk keluar)").lower()

        elif masuikk == "jogja":
            jumlahJog + 1
            masuikk = input("masukkan asal mobil (ketik ""done"" untuk keluar)").lower()

        elif masuikk == "magelang":
            jumlahMag + 1
            masuikk = input("masukkan asal mobil (ketik ""done"" untuk keluar)").lower()


    print ("Jumlah Mobil Solo : ", jumlahSol)
    print ("Jumlah Mobil Surabaya : ", jumlahSur)
    print ("Jumlah Mobil Jogja : ",jumlahJog)
    print ("Jumlah Mobil Magelang : ",jumlahMag)
    



hitung_mobil(masuikk)