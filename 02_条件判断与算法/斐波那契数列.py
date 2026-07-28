# coding = UTF-8

#斐波那契数列

num = int(input("您需要斐波那契数列的几项："))

n1 = 0
n2 = 1
count = 2

if num<= 0:
    print("输入项数错误，请重新输入！")
elif num == 1:
    print("斐波那契数列:", n1)
else:
    # print("斐波那契数列:")
    # print(n1,",",n2, end= " , ")
    # while count < num:
    #     nth = n1 + n2
    #     print(nth, end=" , ")
    #     n1 = n2
    #     n2 = nth
    #     count += 1 
    
    print(n1, n2,end=" ")
    for i in range(1, num-1):
        nth = n1 + n2
        print(nth,end=" ")
        n1 = n2
        n2 = nth

