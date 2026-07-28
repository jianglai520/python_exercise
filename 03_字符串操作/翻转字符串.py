# 翻转字符串

a_str = 'fhgxnicgdshfj'

#法一
print(a_str[::-1])  #翻转
print(a_str[::])

#法二
def func(a_str:str):
    new_str = ''
    for i in range(len(a_str) - 1, -1, -1):   #反向遍历
        new_str += a_str[i]
    return new_str

print(func('abcd'))

