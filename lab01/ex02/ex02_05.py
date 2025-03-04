sogiolam = float(input("Số giờ làm việc TRONG TUAN: "))
luongtheogio = float(input("Lương theo giờ: "))
giotieuchuan = 44
sogiotangca =max(0, sogiolam - giotieuchuan)
Luong = giotieuchuan * luongtheogio + sogiotangca * luongtheogio*1.5

print(F"Lương của bạn là:  {Luong}")