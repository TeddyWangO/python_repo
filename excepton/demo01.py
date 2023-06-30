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

'''
try:
    f = open("D:/OneDriver/OneDrive/桌面/数据类·.txt", "r", encoding="utf-8")
    content = f.readline()
    print(content)
except BaseException as e:
    print(e)
    print("读文件失败！！")