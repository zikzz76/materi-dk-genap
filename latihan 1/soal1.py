#program menentukan apakah sebuah bilangan kelipatan 4
bilangan : int = int(input("masukkan bilangan 4 :"))
if bilangan % 4 == 0 :
    print(f"{bilangan}adalah bilangan 4")
else :
    print(f"{bilangan}bukan bilangan 4")