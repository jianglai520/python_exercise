# coding: UTF-8
#用户输入两个数字，并计算数字之和

num1 = input("请输入第1个数字:")
num2 = input("请输入第2个数字:")

num1 = float(num1)
num2 = float(num2)

sum_up = num1 + num2
print(f"两个数字之和为：{sum_up:.2f}")
