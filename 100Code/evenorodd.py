arr=[3,2,4,5,6]
odd=0
even=0
for i in range(0,len(arr)):
    if arr[i]%2==0:
        even +=1
    else:
        odd +=1
print(odd)
print(even)

