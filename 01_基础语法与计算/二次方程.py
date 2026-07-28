# coding: UTF-8
# 二次方程的解：ax**2 + bx + c = 0
import math

a = float(input("请输入二次方程二次项系数（不等于零）："))
b = float(input("请输入二次方程一次项系数："))
c = float(input("请输入常数项系数："))

key_word = b ** 2 - 4 * a * c

if key_word == 0:
    first_solution = (-b) / (2 * a)
    second_solution = first_solution
    print(f"{a}x**2 +{b}x + {c} = 0的解为:{first_solution}、{second_solution}")
elif key_word > 0:
    first_solution = ((-b) + math.sqrt(key_word)) /(2 * a)
    second_solution = ((-b) - math.sqrt(key_word)) /(2 * a)
    print(f"{a}x**2 +{b}x + {c} = 0的解为:{first_solution}、{second_solution}")
else:
    print(f"{a}x**2 +{b}x + {c} = 0无解")

