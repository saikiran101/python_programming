a=list(map(int,input().split()))
k=int(input())
k=k%len(a)
for i in range(k):
    x=a.pop(-1)
    a.insert(0,x)
print(a)