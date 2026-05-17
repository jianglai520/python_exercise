# 将字符串的时间转换为时间戳

import time 

a1 = '2019-5-10 23:40:00'

timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S")

timeStamp = int(time.mktime(timeArray))
print(timeStamp)

