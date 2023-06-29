"""class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say_age(self,sex):
        self.sex = sex
        print("姓名{0}，年龄{1}，性别{2}".format(self.name,self.age,self.sex))

s = Student('teddy',18)
s.say_age("man")

print(id(Student))
print(type(Student))
print(Student)
print(isinstance(s,Student))
"""
class Student:
    count = 0
    company = 'Sunline'

    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        Student.count+=1
    def say(self):
        print("name:{0},sex:{1},count:{2}".format(self.name,self.sex,Student.count))
s = Student("Teddy","man")
s2 = Student("marry","woman")
s.say()
s2.say()