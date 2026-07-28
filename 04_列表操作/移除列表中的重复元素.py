# coding = UTF-8

#移除列表中的重复元素

a_list = [1, 6, 5, 3, 7, 1, 3, 5]
a_set = set(a_list)
print(list(a_set))

print(list(set(a_list)))  #一步即可