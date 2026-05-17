#定义一个计算器类

class Calculate:

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b
    

a = Calculate()
print(a.add(1, 3))   
print(a.add(1, 5))
print(a.divide(1, 5))
print(a.subtract(3, 5))