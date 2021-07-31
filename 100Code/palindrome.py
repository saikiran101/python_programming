arr=[int(input()) for _ in range(int(input()))]
arr.sort(reverse=True)
for i in arr:
    if str(i)==str(i)[::-1]:
        print("longest palindrome",i)
        break
    else:
        print("no palindrome")
#import sys
#n=int(input("ENTER ARRAY SIZE "))
#arr=[ ]
#for i in range(n):
#    element=int(input())
#    arr.append(element)
#arr.sort(reverse=True)
#for i in arr:
#    if str(i)==str(i)[::-1]:
#        print("longest palindrome ",i)
#        sys.exit(0)
#print("no palindrome exists")