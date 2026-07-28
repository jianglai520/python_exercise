#创建一个类并实例化

class Pet:
    count = 0

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def nameGet(self, name):
        self.name = name 

    def ageGet(self):
        return self.age

pig1 = Pet("peiqi", 12, "公")
print(pig1.name)
print(pig1.gender)
print(pig1.age)
pig1.nameGet('zhu')  #记住：不需要用print包裹
pig1.ageGet()

class Cat(Pet):
    def __init__(self, name, age, gender, sex, time):
        self.name = name
        self.age = age
        self.gender = gender
        self.sex = sex
        self.time = time 
    
    def ageGet(self):
        return f"{self.name}在叫！"  #会覆盖父类方法

cat1 = Cat("mimi", 11, "nan", 2, 3 )    
print(cat1.name) 
print(cat1.ageGet())


    

    
        