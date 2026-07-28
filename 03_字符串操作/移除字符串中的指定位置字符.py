# 移除字符串中的指定位置字符

def fumc(old_str, n):
    length = len(old_str)

    if 0 <= n < length:
        new_str = ""
        for i in range(length): 
           if i != n:
               new_str += old_str[i]
        return new_str
    else:
        print("输入参数错误")

old_str = 'thrqeragly'
print(fumc(old_str,2))
    
    