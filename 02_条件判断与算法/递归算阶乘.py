
def main():
    number = int(input("请输入想阶乘的数字："))
    fact = factorial(number)
    print("{0}的阶乘为：{1}".format(number, fact))

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

if __name__ == '__main__':
    main()
