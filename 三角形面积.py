#coding = UTF-8
#让用户输入三边，计算该三角形面积
import math

a = float(input("请输入第一条边："))
b = float(input("请输入第二条边："))
c = float(input("请输入第三条边："))

cosA = ((b ** 2 + c ** 2) - a ** 2) / (2 * b * c)
sinA = math.sqrt(1 - cosA ** 2)

area = 1/2 * b * c * sinA
print(f"三角形面积为：{area:.1f}")