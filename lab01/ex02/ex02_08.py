def chiahetcho5(sonhiphan):
   stp = int(sonhiphan,2)
   if stp % 5 == 0:
    return True 
   else:
    return False
    
chuoisonhiphan = input("nhap so nhi phan: ")
sonhiphanlist = chuoisonhiphan.split(",")
sochihetcho5 = [so for so in sonhiphanlist if chiahetcho5(so)]
if len(sochihetcho5) > 0:
    ketqua =",".join(sochihetcho5)
    print(ketqua)
else:
    print("khong co so nao chia het cho 5")