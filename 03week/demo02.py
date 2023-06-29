'''class Student:
    company = 'xxx'

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("{0}销毁".format(self))
    @classmethod
    def f1(cls, a):
        print(cls.company)
        print(a)

    @staticmethod
    def f2(c, v):
        print("{0},{1},{2}".format(c, v, (c + v)))


Student.f1('hi')
Student.f2(20, 30)
s = Student('a')
s2 = Student('b')
del s

print("end...")


class Car:
    def __call__(self):
        print("call方法")


c = Car()
c()


class Person:
    def work(self):
        print("xxx")

def work2(s):
    print("good job!!!")
def play_game(s):
    print("play lol")

p = Person()
p.work()
print("===========")
Person.play = play_game
Person.work = work2
p.work()
p.play()



class Person:
    __company = "sun"  # _Person__company

    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def __work(self):
        print("good job")


print(dir(Person))
print(Person._Person__company)
p = Person("zs", 18)
print(p._Person__name)
p._Person__work()



class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def name(self):
        print("姓名:{0}".format(self.__name))
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def salary(self):
        print("薪资:{0}".format(self.__salary))
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary


emp = Employee("Teddy", 300000)
print("姓名：{0}，薪资：{1}".format(emp.name, emp.salary))
emp.name = 'marry'
emp.salary = 5000
print("姓名：{0}，薪资：{1}".format(emp.name, emp.salary))
'''
from dem01 import Student
s = Student("teddy","man")
print(s.name)