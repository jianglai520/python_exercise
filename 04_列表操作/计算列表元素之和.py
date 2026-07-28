# coding = UTF-8

#计算列表元素之和

a_list = [1, 2, 3, 4, 5, 6]

#法一，利用内置函数
total_list = sum(a_list)
print(total_list)

#法二，for循环结构
a = 0
for i in a_list:
    a += i
print(a)

#while循环

i = 0
total = 0
while i < len(a_list):
    total += a_list[i]
    i += 1
print(total)

