#import math
#value = int(input("Enter the Number: "))
#num = [int(d) for d in str(value)]
#sum = 0
#for i in range(0, len(num)):
#    sum = sum + math.pow(num[i], len(num))

#if sum == value:
#    print("Given number is Armstrong Number")
#else:
#    print("Given Number is not Armstrong Number")

import math
first=int(input("enter f"))
second=int(input("enter second"))
def armstrong(value):
    num = [int(d) for d in str(value)]
    sum = 0
    for i in range(0, len(num)):
        sum = sum + math.pow(num[i], len(num))

    if sum == value:
        print("Given number is Armstrong Number",value)
    else:
        print("Given Number is not Armstrong Number",value)

for i in range(first, second +1):
    armstrong(i)
