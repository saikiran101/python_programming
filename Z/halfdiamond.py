num=int(input("enter the number: "))
k=3
for i in range(0,num):
    for j in range(0,i+1):
        print(k,end="")
    k+=1
    print()
k=k-2
for i in range(1,num):
    for j in range(0,num-i):
        print(k,end="")
    k-=1
    print()
    