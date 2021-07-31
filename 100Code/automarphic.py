n=int(input())
sum=1
for i in range(2,n):
    if n%i==0:
       sum +=i
print(sum)

if sum>n:
    print("abundant")
else:
    print("not abundant")
