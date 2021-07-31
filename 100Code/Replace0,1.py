num=(input("enter number"))#5000
num1=""
for i in range(0,len(num)):
    if num[i] == "0":
        num1=num1 +"1"
    else:
        num1=num1 + num[i]
print("output",num1)

#5001
#5111