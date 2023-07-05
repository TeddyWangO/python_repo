'''
while True:
    try:
        a = int(input("请输入："))
        if a ==5:
            print("end")
            break
    except BaseException as e:
        print(e)

try:
    print("step1")
    a = 3/0
    print("step2")
except BaseException as e:
    print("step3")
    print(e)


try:
    n = input("被除数：")
    m = input("除数：")
    c = float(n)/float(m)
except BaseException as e:
    print(e)
else:
    print("商：",c)
finally:
    print("我是大哥")
    #


try:
    f = ope(n"D:/OneDriver/OneDrive/桌面/数据类·.txt", "r", encoding="utf-8")
    content = f.readline()
    print(content)
except BaseException as e:
    print(e)
    print("读文件失败！！")


with open("D:/OneDriver/OneDrive/桌面/数据类.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line,end="\t")

import traceback

try:
    print("step1")
    with open("D:/OneDriver/OneDrive/桌面/数据类1.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="\t")
except BaseException as e:
    with open("D:/OneDriver/OneDrive/桌面/log.txt","a") as f:
        traceback.print_exc(file=f)

'''

class AgeError(Exception):
    def __init__(self,errorInfo):
        Exception.__init__(self)
        self.errorInfo = errorInfo

    def __str__(self):
        return str(self.errorInfo)+".非法年龄"

if __name__ == "__main__":

        age = int(input("你的年龄："))
        if age<0 or age>150:
            raise AgeError(age)
        else:
            print("年龄",age)
