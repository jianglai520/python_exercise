# 计算数组元素之和

a_list = [1, 2, 3, 4, 5]
print(sum(a_list))

a = 0
for i in a_list:
    a += i
print(a)

a = 0
i = 0
while i < len(a_list):
    a += a_list[i]
    i += 1
print(a)