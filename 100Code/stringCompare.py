from datetime import datetime
first=datetime.now()
a="labe"*100000
b="bela"*100000
if len(a)!=len(b):
    print("not match")
else:
    a=sorted(a)
    b=sorted(b)
    if a == b:
        print("string matched")
    else:
        print("not matched")
last=datetime.now()
print(last-first)