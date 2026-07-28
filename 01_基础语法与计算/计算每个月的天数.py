# coding =UTF-8

#计算每个月的天数

import calendar

print(calendar.monthrange(2025, 11))   #输出为一个元组，第一个元素为每个月的开头第一天的星期数，第二个为天数

a = calendar.monthrange(2025, 11)
print(a)

