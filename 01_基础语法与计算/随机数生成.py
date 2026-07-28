#coding = UTF-8
#随机数的生成练习
import random

print(random.randint(1, 19)) #生成1~19(包含1和19)之间的整数

print(random.random())  #生成介于0.0到1.0之间的随机小数

list_1 = [1, 2, 3, 4, 5]
print(random.choice(list_1))   #从序列中任意选择一个元素

random.shuffle(list_1)  #对序列进行随机排序
print(list_1)

