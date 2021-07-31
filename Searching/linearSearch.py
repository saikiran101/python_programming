def LinearSearch(list,n,key):
    for i in range(0,n):
        if(list[i]==key):
            return i
    return -1

list=[1,2,3,6,5,4]
n=len(list)
key=4
res=LinearSearch(list,n,key)
if (res==-1):
    print("not found")
else:
    print('found',res)
