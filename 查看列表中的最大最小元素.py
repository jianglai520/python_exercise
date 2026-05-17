# coding = UTF-8

#查看列表中的最大元素与最小元素

a_list = [1, 4, 7, 5, 6]

print(f"列表中最大元素为：{max(a_list)}，最小值为{min(a_list)}")

#内置高阶函数
print(sorted(a_list))
a = sorted(a_list)
print(a[0])     # min
print(a[-1])    # max

#列表内置方法
a_list.sort()
print(a_list[-1])  #max
print(a_list[0])   #min