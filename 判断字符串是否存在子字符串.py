def func(str_, part_str):
    if part_str in str_:
        print(f"{part_str}是{str_}的字符串")
    else:
        print(f"{part_str}不是{str_}的字符串")

str_ = "abb.acc.fhgjhggjhj"
part_str = "abb"
func(str_, part_str)


    