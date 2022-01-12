rows=int(input("print rows: "))
cols=int(input("print cols: "))
for i in range(0, rows):
    for j in range(0,rows-i-1):
        print(" ",end=" ")
    for j in range(0,cols):
        print("*", end=" ")
    print()
