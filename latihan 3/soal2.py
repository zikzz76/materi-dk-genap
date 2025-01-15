#program menentukan hadiah
belanja=int(input("masukan nilai pembelian pelanggan :"))

if belanja < 1500000 and belanja < 5000000 :
 print("SELAMAT ANDA MENDAPATKAN TV BRACKET")
elif belanja > 5000000 :
    print("SELAMAT ANDA MENDAPATKAN SOUND BAR")
else :
    print("tidak ada hadiah")    