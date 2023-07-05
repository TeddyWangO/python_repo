'''f = open(r"d:\a.txt","a")
f.write("append")
f.close()

with open(r"d:\a.txt","a") as f:
    f.write("append")
    f.close()

with open(r"a.txt","a",encoding="utf-8") as f:
    f.write("中文乱码")
    f.close()

with open(r"b.txt","w") as f:
    f.write("Teddy\n27\n河南")

with open(r"b.txt","r",encoding="GBK") as f:
    # content = f.read(4)
    # print(content)
    # print(f.read())
    # content = f.read()
    # print(content)
    # content = f.readline()
    # print(content)
    # content = f.readlines()
    # print(content)
    # for line in f:
    #     print(line,end="")
    while True:
        line = f.readline()
        if line:
            print(line,end="")
        else:
            break

with open(r"b.txt","r",encoding="GBK")as f:
    lines = f.readlines()
    result = [line.rstrip()+"\t#"+str(index)+"\n" for (index,line) in zip(range(0,len(lines)),lines)] #并行遍历

# with open(r"b.txt","w",encoding="GBK") as ff:
#         ff.writelines(result)
    with open(r"b.txt", "w", encoding="GBK") as ff:
        for content in result:
            ff.write(content)


with open(r"img.png","rb") as recourse,open(r"target.png","wb") as target:
    for result in recourse:
        target.write(result)

'''

with open("e.txt","r",encoding="utf-8") as f:
    print("文件名是：{0}".format(f.name)) #文件名是：e.txt
    print(f.tell())  #0
    print("读取的内容：{0}".format(str(f.readline()))) #读取的内容：abcdefghijklmn
    print(f.tell()) #14
    f.seek(3, 0)
    print("读取的内容：{0}".format(str(f.readline()))) #读取的内容：defghijklmn


