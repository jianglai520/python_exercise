my_dict = {'trudge':1, 'shabby':2, 'poet':3, 'thonry':4, 'indictment':5}

print(my_dict)
print(str(my_dict))
print("原始字符串为:" + str(my_dict))
#print("原始字符串为:" + my_dict)   #错误表述

del my_dict['trudge']   #移除没有的 key 会报错
print("字典移除后：" + str(my_dict))
