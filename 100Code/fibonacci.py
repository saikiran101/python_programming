def fibonacci(i):
    if i<=1:
        return i
    else:
        return fibonacci(i-1)+ fibonacci(i-2)


num=int(input())
if num <= 0:
    print("postiver numbers")
else:
    print("fibonacci series",end=" ")
    for i in range(num):
        print(fibonacci(i),end=",")