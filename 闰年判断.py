# coding = UTF-8

#用户输入年份，判断是否为闰年
#能被400整除，或能被4整除但不被100整除的年份就是闰年

year = int(input("请输入年份："))

if year % 4 == 0:
    if year % 100 != 0:
        if year % 400 == 0:
            print(f"{year}为闰年")
        else:
            print(f"{year}为平年")
    else:
        print(f"{year}为闰年")
else:
    print(f"{year}是平年")

