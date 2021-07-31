#size=int(input())
#arr=[]
#for i in range(size):
#    element=int(input())
#    arr.append(element)
#print("print min",min(arr))
#arr=[5,2,10,200]
#arr1=sorted(arr)
#print(max(arr1[:-1]))
#size=list(int(input("enter")))
arr = [int(input()) for _ in range(int(input()))]
x=[]
y=[]
n=len(arr)
for i in range(n//2):
    x.append(arr[i])
for i in range(n//2,n):
    y.append(arr[i])
x.sort()
print(x)
y.sort(reverse=True)
print(y)
print(x+y)
