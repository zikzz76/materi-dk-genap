#program game tebak angka
print("selamat datang di program tebak angka")
angka = 15
tebakan = int(input("masukan angka yang kamu tebak :"))
if tebakan < angka :
    print("tebakan kamu terlalu kecil")
elif tebakan > angka :
    print("tebakan kamu terlalu besar")
else :
    print("tebakan kamu benar")