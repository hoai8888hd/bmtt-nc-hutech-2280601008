import ast
def xoapt(dict,key):
    if key in dict:
        del dict[key]
        return True
    else:
        return False
my_dict = {'a':1,'b':2,'c':3}
keytodel = 'a'
kq = xoapt(my_dict,keytodel)
if kq:
    print("sau khi xoa: ",my_dict)
else:    
    print("key khong ton tai")