# 递归

# def main():
#     message(5)

# def message(times):
#     if times > 0:
#         print("hyhhh")
#         message(times - 1)

# if __name__ == '__main__':
#     main()


# def func(num):
#     if num <= 0:
#         print("不符合要求")
#     elif num == 1:
#         return 0
#     elif num == 2:
#        return 0, 1
#     else:
#         for i in range(1, num + 1):
#             return func(num - 1) + func(num - 2)

# print(func(3))


#斐波那契数列使用递归
def main():
    num = int(input("请输入你需要的斐波那契的项数："))
    print(f"前{num}项的斐波那契数列为：")

    for i in range(1, num + 1):
        print(fib(i))

def fib(num):
    if num <= 0:
        return "输入值错误"
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)
if __name__ == '__main__':
    main()

