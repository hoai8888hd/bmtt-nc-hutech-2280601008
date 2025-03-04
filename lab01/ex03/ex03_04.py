def truycapphantu(tupple_data):
    st_element = tupple_data[0]
    nd_element = tupple_data[-1]
    return st_element, nd_element
input_tuple = eval(input("nhap tuple: "))
first, last = truycapphantu(input_tuple)
print("phan tu dau tien: ", first)
print("phan tu cuoi cung: ", last)