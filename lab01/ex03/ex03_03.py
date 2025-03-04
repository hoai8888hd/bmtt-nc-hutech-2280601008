def taotupletuple(list):
    return tuple(list)
input_list = input("nhap danh sach: ")
num = list(map(int, input_list.split(' ')))

mytuple = taotupletuple(num)
print("list: ",num)
print("tuple: ",mytuple)