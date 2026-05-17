#coding = UTF-8
#摄氏温度转换华氏温度

celsius = float(input("请输入摄氏温度："))

fahrenheit = celsius * 1.8 + 32
print(f"{celsius}摄氏度为{fahrenheit:1f}华氏度")