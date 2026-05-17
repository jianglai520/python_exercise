# coding = UTF-8
# 用户输入一个数字，计算它的平方根

num = float(input("请输入一个整数："))

if num == 0:
    print(f"{num}的平方根为:0")
if num > 0:
    sqrt_num = num ** (1 / 2)
    print(f"{num}的平方根为:{sqrt_num:.3f}")
else:
    print("没有算术平方根！")