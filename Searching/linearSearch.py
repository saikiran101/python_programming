def linearsearch(list,n,key):
    for i in range(0,n):
        if list[i]==key:
            return i
    return -1

list=[2,3,4,5,6]
n=len(list)
key=100
res=linearsearch(list,n,key)
if res==-1:
    print("not found")
else:
    print("found")
