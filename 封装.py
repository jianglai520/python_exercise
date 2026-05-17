class Pet:
    __count = 0

    def __init__(self, age, gender, name):
        self._age =  age
        self._gender = gender
        self._name = name

    def getName(self, name):
        self._name = name 

    def setName(self):
        return self._name
    
    def setAge(self):
        return self._name
    
    classmethod
    def calCount(cls):
        cls.__count += 1
        return cls.__count
    
    staticmethod
    def addNumber(a, b = 10):
        res = a + b
        return res
    
    def default():
        print(f"本地方法：{Pet.__count}")
    
    property
    def comInfo(self):
        info = f"{self._name}, {self._age}, {self._gender}"

print(dir(Pet))
stu1 = Pet(18, "男", 'Jack')
print(stu1._name)
print(stu1._age)
print(stu1._gender)
print(stu1.setName())
print(stu1.calCount())
print(stu1.comInfo)