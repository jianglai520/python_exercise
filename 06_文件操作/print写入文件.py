#print写入文件

fw = open(r"C:\Users\如玧\Desktop\练习.txt", "w", encoding = "ANSI")

print("张三", end = " ", file = fw)
print("李四", file = fw)
print("小刚", end = " ",file = fw)
print("萧然", file = fw)

d = {"abd":"123", "cde":"456"}

fw.writelines(d)
fw.writelines("\n")

for key, value in d.items():
    fw.writelines(f"{key}:{value}\n")

fw.writelines("\n")
print("\n", file = fw)

fw.close()