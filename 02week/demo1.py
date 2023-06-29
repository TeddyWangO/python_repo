"""

def add(a, b, c):
    sum = a + b + c
    return sum


print(add(1, 2, 3))



def print_max(a, b):

    if (a > b):
        print(a)
    help(print_max)
    print(print_max.__doc__)


print_max(10, 5)


def print2(n):
    print("*" * n)


print2(5)

g = 100
def f1():
    a,b,c = 5,8,10

    global g
    g = 50
    print(locals())

f1()
print(g)

"""
import time

a = 100
def test01():
    stat = time.time()
    global a
    for i in range(10000000):
        a+=1
    end = time.time()
    print("spend:{0}".format(end-stat))
def test02():
    b = 100
    stat = time.time()

    for i in range(10000000):
        b+=1
    end = time.time()
    print("spend:{0}".format(end-stat))

test01()
test02()