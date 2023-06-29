'''
a = {}
print(a)
b = {"name":"teddy","age":"18","age":"38"} # key相同，覆盖
print(b)
print(b["age"])
c = dict(name = 'teddy',age = '18')
print(c)
e = dict([("name","teedy"),("age","18")])
print(e)
k = ["name","age"]
v = ["teddy","18"]
d = dict(zip(k,v))
print(d.items())
f = dict.fromkeys(["name","age"])
print(f)


a = {"name":"teddy","age":"18","job":"coder"}
print(a["name"])
print(a.get("ageq"))
print(a.items())
print(a.keys())
print(a.values())
print("name" in a)
print("ter" in a)


a = {"name":"teddy","age":"18","job":"coder"}
# a["addr"] = "SZ"
# print(a)
b = {"name":"tom","age":"38","job":"coder","money":"180000"}
a.update(b)
print(a)

b = {"name":"tom","age":"38","job":"coder","money":"180000"}
# b.pop("money")
# b.clear()
b.popitem()
print(b)


b = {"name":"tom","age":"38","job":"coder","money":"180000"}
# a,c,d,e = b.values()

# a,c,d,e = b
a,c,d,e = b.items()
print(a)
print(c)
print(d)
print(e)

b1 = {"name":"tom","age":"38","job":"coder","money":"180000"}
b2 = {"name":"marry","age":"18","job":"coder","money":"380000"}
b3 = {"name":"jack","age":"28","job":"coder","money":"280000"}
b4 = {"name":"da","age":"48","job":"coder","money":"80000"}

tb = [b1,b2,b3,b4]

print(tb)
for i in range(len(tb)):
    print(tb[i].get("name"))

'''

