def daonguoclist(lst):
    return lst[::-1]
input_list = input("nhap danh sach: ")
num = list(map(int, input_list.split(' ')))
daonguoc = daonguoclist(num)
print(daonguoc)