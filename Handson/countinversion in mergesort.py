def countinversion(arr,n):
    temp_arr=[0]*n
    return mergesort(arr,temp_arr,0,n-1)
def mergesort(arr,temp_arr,left,right):
    in_count=0
    if left<right:
        mid=(left+right)//2
        in_count+=mergesort(arr,temp_arr,left,right)
        in_count+=mergesort(arr,temp_arr,mid+1,right)
        in_count+=merge(arr,temp_arr,left,mid,right)
    return in_count
def merge(arr,temp_arr,left,mid,right):
    i=left
    j=mid+1
    k=left
    in_count=0
    while i<=mid and j<=right:
        if arr[i]<=arr[j]:
            temp_arr[k]=arr[i]
            k+=1
            i+=1
        else:
            temp_arr[k]=arr[j]
            in_count+=mid-i+1
            k+=1
            j+=1
    while i<=mid:
        temp_arr=arr[i]
        k+=1
        i+=1
    while j<=right:
        temp_arr=arr[j]
        k+=1
        j+=1
    for i in range(left,right+1):
        arr[i]=temp_arr[i]
    return in_count

arr=[3,5,2,1,6]
n=len(arr)
res=countinversion(arr,n)
print(res)

