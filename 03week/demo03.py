'''
class Person:
    def __init__(self, name, sex):
        self.__name = name
        self.__sex = sex

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        self.__sex = sex


class Student(Person):
    def __init__(self, name, sex, age):
        # Person.__init__(self, name, sex)
        super(Student, self).__init__(name, sex)
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


s = Student("marry", "women", "18")
print(s.name)
print(s.sex)
print(s.age)

print(Student.mro())


class A:
    def aa(self):
        print("aa")
    def say(self):
        print("AA")
class B:
    def aa(self):
        print("bb")

    def say(self):
        print("BB")
class C(B,A):
    def cc(self):
        print("cc")
c = C()
print(C.mro())
c.say()
c.aa()


class A:
    def __init__(self):
        print("A的构造方法")
    def say(self):
        print("say:AA")
class B(A):
    def __init__(self):
        super(B,self).__init__()
        A.__init__(self)

        print("B的构造方法")
    def say(self):
        super().say()
        A.say(self)
        print("say:BB")

b = B()
b.say()

class Animals:
    def shout(self):
        print("动物叫了一声")

class Dog(Animals):
    def shout(self):
        print("Dog:汪汪汪")

class Cat(Animals):
    def shout(self):
        print("Cat:咪咪咪")
def animalShout(a):
    a.shout()

animalShout(Dog())
animalShout(Cat())



class Person:
    def __init__(self,name):
        self.name = name

    def __add__(self, other):
        if isinstance(other,int):
            print("{0}".format(self.name)*other)

p = Person("Teddy")
p.__add__(3)


import copy

class Test:
    def __init__(self,cpu):
        self.cpu= cpu
class Cpu:
    pass

c = Cpu()
t=Test(c)
t1 = copy.copy(t)
print("浅拷贝")
print(id(t))
print(id(t1))
print(id(t.cpu))
print(id(t1.cpu))
t2 = copy.deepcopy(t)
print("深拷贝")
print(id(t))
print(id(t2))
print(id(t.cpu))
print(id(t2.cpu))

class Cpu:
    def cal(self):
        print("cpu超赛")

class Screen:
    def show(self):
        print("联想")

class Oppo:
    def __init__(self,cpu,screen):
        self.cpu = cpu
        self.screen = screen

c = Cpu()
s = Screen()
o = Oppo(c,s)
o.cpu.cal()
o.screen.show()


class BZ:pass
class BM:pass
class BYD:pass
class Factory:
    def create(self,name):
        if name == "BMW":
            return BM()
        elif name == "DB":
            return BZ()
        elif name == "DD":
            return BYD()
        else:
            print("error")

f = Factory()
print(f.create("DD"))

f.create("DDA")


class MySingle:
    __obj = None
    __objTag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
        return cls.__obj
    def __init__(self,name):
        if self.__objTag:
            print("调用构造方法")
            self.name = name
        self.__objTag = False

m = MySingle("mm")
m2 = MySingle("qq")
print(id(m))
print(id(m2))
'''
class BZ:pass
class BM:pass
class BYD:pass
class Factory:
    __obj = None
    __init_Flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
        return cls.__obj
    def __init__(self):
        if self.__init_Flag:
            self.__init_Flag = False
    def create(self,name):
        if name == "BMW":
            return BM()
        elif name == "DB":
            return BZ()
        elif name == "DD":
            return BYD()
        else:
            print("error")

f = Factory()
print(f.create("DD"))
print(f.create("BMW"))
f2 = Factory()
print(f2.create("DD"))
print(f2.create("BMW"))

print(f)
print(f2)