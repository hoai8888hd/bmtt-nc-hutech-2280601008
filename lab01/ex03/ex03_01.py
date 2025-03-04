def tongchan(list):
    sum = 0
    for i in list:
        if i % 2 == 0:
            sum += i
    return sum

input_list = input("nhap danh sach: ")
num = list(map(int, input_list.split(' ')))
tinhtongchan = tongchan(num)
print(tinhtongchan)