"""
b = [10,20]
def test(m):
    print(m)
    print(id(m))
    m.append(30)

test(b)
print(id(b))
print(b)


a = 100
def test(n):
    print(id(n))
    print(n)
    n = n + 100
    print(n,id(n))
test(a)
print(a)


import copy
def test():
    a = [1, 2, ['x', 'u']]
    b = copy.copy(a)
    print(a,id(a),id(a[2]))
    print(b,id(b),id(b[2]))
    print("浅拷贝，修改b")
    b.append('copy')
    b[2].append("99")
    print(a, id(a), id(a[2]))
    print(b, id(b), id(b[2]))
test()

a = (10,20,[5,6])
print(a,id(a))
def test(m):
    print(m,id(m))
    m[2][0] = 888
    print(m,id(m),id(m[2][0]))
test(a)
print(a,id(a),id(a[2][0]))

def test(a,b,*c):
    print(a,b,c)
test(1,2,3,4,5,6)

def f1(*a,b,c):
    print(a,b,c)
f1(1,2,3,b = 5,c = 6)

def f2(a,b,**c):
    print(a,b,c)

f2(1,2,name='teddy',age=18)
def f3(a,b,**c):
    print(a,b,c)

f3(1,2,name='teddy',age=18)

def f4(a,b,*c,**d):
    print(a,b,c,d)
f4(1,2,3,4,5,name='sarry',age=19)

a = lambda a,b,c:a+b+c
print(a)
print(id(a))
print(a(1,2,3))

g = [lambda a:a*2,lambda b:b*3,lambda c:c*4]

print(g[0](2),g[1](3),g[2](3))



s = "print('abc')"
eval(s)
a = 10
b = 20
c = "print(a+b)"
eval(c)
d = dict(a=100,b=200)
e = eval("a+b",d)
print(e)

def f(n):
    print("start:"+str(n))
    if n == 1:
        print("递归结束")
    else:
        f(n-1)
    print("end:"+str(n))
f(3)


n = int(input("input:"))
def f2(m):
    if m ==1:
        return 1
    else:
        return m*f2(m-1)
print(f2(n))


def out():
    print("out running")
    def inner():
        print("inner running")
    inner()
out()

def printName(isChineseName,name,firstName):

    def icorePrint(a,b):
        print("{0} {1}".format(a,b))
    if isChineseName:
        icorePrint(firstName,name)
    else:
        icorePrint(name,firstName)

printName(True,"启迪","王")
printName(False,"Teddy","Wang")

"""
a = 10
def out():
    b = 20

    def inner():
        nonlocal b
        b = 0
        print("inner{b}".format(b=b))
        global a
        a = 1
        print("inner{a}".format(a=a))
    inner()
    print("out{0}{1}".format(a,b))
out()
print(a)
