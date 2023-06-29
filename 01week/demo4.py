"""
n = input("shuru:")
if int(n)<10:
    print(n+"<10")
else:
    print(n+">10")
if 1:
    print("非0整数为true")
a = []
if a:
    print("空集合，列表，元组，字典为false")
else:
    print("集合，列表，元组，字典为空")
b = ()
if b:
    print("空集合，列表，元组，字典为false")
else:
    print("集合，列表，元组，字典为空")

if 1 < 5 < 9:
    print("TRUE")

n = input("请输入整数：")
m = input("请输入整数：")

q = (n if n<m else m)
print(q)

score = input("请输入成绩：")
grade = ''
if int(score) <60:
    grade = "不及格"
elif 60<=int(score)<70:
    grade = "及格"
elif 70<=int(score)<80:
    grade = "达标"
elif 80<=int(score)<90:
    grade = "良好"
elif 90<=int(score)<100:
    grade = "优秀"
else:
    grade = "输入不合法"
print(grade)


score = int(input("请输入成绩："))
grade = ''
if score>100 or score<0:
    print("请重新输入：")
else:
    if score>=90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score < 60:
        grade = "E"
print(grade,score)


n = int(input("请输入："))
m = int(input("请输入："))
sum = 0
while n<m:
    print("{0}<{1}".format(n,m))
    n+=1
    sum += n;
print(n,m,sum)

for x in (10,20,30):
    print(x*6)

a = [i for i in range(10)]
print(a)

sum = 0
jis = 0
os = 0

for i in range(101):
    sum+=i
    print(sum)
    if i%2==0:
        jis+=i
    else:
        os+=i
print(sum,jis,os)


for i in range(5):
    for j in range(5):
        print(i,end="\t")
    print("")

result = 0
for i in range(1,10):
     for j in range(1,10):
        result = i*j;
        print("{0}*{1}={2}".format(i,j,result),end="\t")
        if i==j:
            break
     print()
for i in range(1,10):
     for j in range(1,1+i):
        result = i*j;
        print("{0}*{1}={2}".format(i,j,result),end="\t")

     print()

b1 = {"name":"tom","age":"38","job":"coder","money":"18000"}
b2 = {"name":"marry","age":"18","job":"coder","money":"3800"}
b3 = {"name":"jack","age":"28","job":"coder","money":"2800"}
b4 = {"name":"da","age":"48","job":"coder","money":"8000"}

tb = [b1,b2,b3,b4]
# for x in tb:
#     if int(x.get("age"))>18:
#         print(x)
for x in tb:
    if int(x.get("money"))>8000:
        print(x)

"""


















 








