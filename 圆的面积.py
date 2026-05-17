#coding = UTF-8
#用户输入半径，计算圆的面积
import math

r = float(input("请输入圆的半径："))

s = math.pi * (r ** 2)
print(f"半径为{r}的圆的面积为：{s:.2f}")