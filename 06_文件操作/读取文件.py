#读取文件内容

with open(r"C:\Users\如玧\Desktop\练习.txt", "r", encoding="ANSI") as file:
    line1 = file.readline()
    line2 = file.readline(2)
    file.seek(0)
    contents = file.read()


print(contents)
print(f"第一行为{line1}\n")
print(f"第二行前2个数据为{line2}\n")