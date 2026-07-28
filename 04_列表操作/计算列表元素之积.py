# coding = UTF-8

#计算列表元素之积

a_list = [1, 2, 3, 4]

#for循环
a = 1
for i in a_list:
    a *= i
print(a)

#while循环
a = 1
i = 0
while i < len(a_list):
    a *= a_list[i]
    i += 1
print(a)
    
