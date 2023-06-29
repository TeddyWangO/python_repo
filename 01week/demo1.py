import io

# a = "aaaaadsds\
# dasdasd"
# print(a)
'''a = 3
print(id(a))
print(type(a))
print(a)
b, c, d = 1, 3, 4
print(b, c, d)
print(divmod(14, 6))

a1 = 10 ** 1000
print(a1)

a3 = 5 < 10 < 33
print(a3)

d1 = 'i love u'
print(len(d1))
print(d1 * 10)

c = 333
e = 333
print(c is e)

a2 = [1, 2, 5, 3]
a3 = 2
print(a3 in a2)

# myName = input("请输入：")
# print("my name is "+myName)

myStr = 'asdzxcvbngrrt'

myStr = myStr.replace('a', '啊')

print(str(myStr))
print(myStr[::-1])
print(myStr[:-1])

d = "name is {0},age is {1}".format("teddy", 20)
print(d)
f = "name is {name},age is {age}".format(age=18, name="Tom")
print(f)
e = "name is {0},age is {1:.2f},salary is {0}".format("Tom",20.2355)
print(e)
g = 'asdfghjjk'
print(id(g))
g = io.StringIO(g)
g.seek(2)
g.write('11')
print(g.getvalue())
print(id(g))

a =[ i for i in range(10) if i % 3==0]
print(a)


a = [10,20,30]
b = [1,2,3]
# a = a+b

# a.extend(b)
# a.append(b)
# a.insert(0,100)
# del(a[2])
# a.remove(10)
a.pop(2)
print(a)
'''
'''
a = [1, 2, 3, 4, 5, 6, 8, 8, 8, 9, 1]
print(a[0])
print(a.index(8,7))
print(a.count(8))
print(len(a))
print(100 in a)
print(100 not in a)

a = [1, 2, 3, 4, 5, 6, 8, 8, 8, 9, 1]
# print(a[::-1])
# print(a[-3:])
# print(a[-3:-1])
# print(a[0:5])
#
# for i in range(len(a)):
#     print(a[i])

# for obj in a:
#     print(obj)
# b = [] +a
# print(id(a))
# print(id(b))
b = [9,8,2,4,6,3,5]
# b.sort()
# b.reverse()
a = sorted(b)
print(a)
print(b)
print(max(a))
print(min(a))
print(sum(a))


a = [
    ["tom  ", "bj", "10000", "18"],
    ["marry", "sz", "18000", "28"],
    ["mate ", "sh", "15000", "19"]
]
# print(a[0][1])
# print(a[1][0])
# print(a[2][2])
for n in  a :
    for i in n:
        print(i,end='\t')
    print()
# for n in range(len(a)):
#     for m in range(4):
#         print(a[n][m],end='\t')
#     print()



# a = (10,20,30)
# b = 40,50,60
# c = 100,
# print(type(a))
# print(type(b))
# print(type(c))
#
# a1 = tuple()
# a2 = tuple("asbc")
# a3 = tuple([1,2,2])
# print(type(a1))
# print(type(a2))
# print(type(a3))

# a = (n for n in range(5))
# b = tuple(a)
# c = tuple (a)
# print(b.__repr__())
# print(a.__next__())
# print(a.__next__())
#
# print(a.__next__())
b = tuple("abc")
c = tuple(range(3))
d = tuple([2,3,4])
print(b)
print(c) 
print(d)
    
'''
