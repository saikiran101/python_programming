def countinversions(arr,n):
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                count+=1
    return count


arr=[20,4,1,5,6]
n=len(arr)
res=countinversions(arr,n)
print(res)