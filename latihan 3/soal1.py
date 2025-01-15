#program menghitung nilai akhir
print("PROGRAM MENGHITUNG NILAI AKHIR")
tugas=float(input("masukan nilai tugas :"))
uas=float(input("masukan nilai uas :"))
uts=float(input("masukan nilai uts :"))

#mengecek 
nilai_akhir = (0.3 * tugas) + (0.5 * uas) + (0.2 * uts)
#hasil
print("nilai akhir",nilai_akhir)