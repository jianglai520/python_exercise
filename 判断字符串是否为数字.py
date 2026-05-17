# coding = UTF-8

#判断字符串是否为数字

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

print(is_number('fool'))
print(is_number('1000000000'))
print(is_number('-1e3'))
print(is_number('-1.23333333333'))

#测试 Unicode
print(is_number('四'))
