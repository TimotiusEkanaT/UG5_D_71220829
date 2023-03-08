import math
jark = input("Masukkan jarak awal (dalam meter): ")
el1 = input("Masukkan sudut elevasi pada menit ke-5 (dalam derajat): ")
el2 = input("Masukkan sudut elevasi pada menit ke-6 (dalam derajat): ")
awal = jark * math.tan(math.radians(el1))
akhir = jark * math.tan(math.radians(el2)) - math.tan(math.radians(el1))
selisih = jark * math.tan(math.radians(el2))
print ("Selisih ketinggian drone saat menit ke-5 dan ke-6 adalah",selisih,"meeter")
