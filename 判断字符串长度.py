# coding = UTF-8

#判断字符串的长度

#法一
a = 'hhchuffjhg'
print(f"字符串{a}的长度为:{len(a)}")

#法二
def get_len(str):
    i = 0
    while str[i:]:
        i += 1
    return i

str ="hhfjgiehg"
print(get_len(str))