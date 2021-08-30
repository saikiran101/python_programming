star=int(input("enter the size to display a star: "))
for i in range(0,star):
    for j in range(0,star-i-1):
        print(" ",end=" ")
    for j in range(0,i*2+1):
        print("*",end=" ")
    print()
