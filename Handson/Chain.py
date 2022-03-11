from collections import ChainMap

d1={"a":1,"b":2}
d2={"c":3,"d":4}
d3={"d":5,"e":6}
c=ChainMap(d1,d2,d3)

print(c["a"])

print(c.values())

print(c.keys())

for key,value in c.items():
    print(key)
