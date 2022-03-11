n=list(map(int,input().split()))
sum=0
for val in range(0,len(n)):
    sum +=sum + n[val]

print(sum)
print(n)
#num=list(int(input("enter list")))