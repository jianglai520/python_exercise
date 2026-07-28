#写入文件

def demo():
    txt = "是否继续输入，'是'输入1，否则按回车："
    total = 0
    fw = open(r"C:\Users\如玧\Desktop\练习.txt", 'w', encoding = "ANSI")

    while True:
        if input(txt):
            name = input("请输入名字：")
            total += fw.write(name + "\n")
        else:
            break

    fw.close()
    print(f"共输入{total}个字符（含换行符）")

demo()