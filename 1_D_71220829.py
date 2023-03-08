def ganti_kata(asdh, buasihf, oihsdg):
    ohasf = asdh.split(" ")
    for cc in ohasf:
        if cc == buasihf :
            # huahs = ohasf.index(cc)
            buasihf[cc] = oihsdg
            hoasd = ' '.join(ohasf)
    return hoasd

asdh = input("Masukkan kalimat : ")
buasihf = input ("Kata yang dicari : ")
oihsdg = input ("Diganti menjadi : ")
print (ganti_kata(asdh, buasihf, oihsdg))