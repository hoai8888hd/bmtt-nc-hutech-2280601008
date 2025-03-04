def demsolanxuat(list):
    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

input_str = input("nhap chuoi: ")
wlist=input_str.split()
solanxuathien=demsolanxuat(wlist)
print(solanxuathien)