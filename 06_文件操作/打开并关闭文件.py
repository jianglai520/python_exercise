#基本文件练习

fileName1 = r"C:\Users\如玧\Desktop\练习.txt"

fileObj1 = open(fileName1, "w")
fileObj1.write("方法1:打开&手动关闭")

fileObj1.close()
