def ratcount(arr,n,r,unit):
    if n==0:
        return -1
    totalfood=r*unit
    h=0
    sum=0
    for i in range(0,n):
        sum+=arr[i]
        if sum>=totalfood:
            return i+1
    return 0
arr=[2,8,3,5,7,4,1,2]
n=len(arr)
r=7
unit=2
res=ratcount(arr,n,r,unit)
print(res)