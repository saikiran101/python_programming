from collections import namedtuple


student =namedtuple("student",["name","age","dob"])
s= student("jahnavi","22","07")
print(s[1])
print(s.name)#nametuple