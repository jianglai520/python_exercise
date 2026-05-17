# coding = UTF-8

x = input("请输入x的值：")
y = input("请输入y的值：")

exchange = x
x = y
y = exchange

print(f"交换后的x的值为：{x}")
print(f"交换后的y的值为：{y}")