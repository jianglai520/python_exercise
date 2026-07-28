#f.writelines(iter)

fw = open(r"C:\Users\如玧\Desktop\练习.txt", 'w', encoding = "ANSI")

fw.writelines(("张三\n", "李四\n"))
fw.writelines(["王五\n", "小明\n"])
fw.writelines({"小赵\n", "小刚\n"})

d = {"abc":"aaa", "efg":"eee"}

fw.writelines(d)
fw.writelines("\n")
for key, value in d.items():
    fw.writelines(f"{key}:{value}\n")

fw.writelines("\n\n\n")
fw.writelines("单一字符也可以写入\n")

fw.close()