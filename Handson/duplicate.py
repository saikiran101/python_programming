
def freq(arr,n):
    d=dict()#empty

    for i in range(n): #0-7 loop
        if arr[i] in d.keys():#repeated values
            d[arr[i]] +=1 
        else:
            d[arr[i]] =1 #unique

    for x in d:
        print(x," ",d[x]) #to print value and freq

arr=[10,20,20,10,10,20,5,20]
n=len(arr)
ans= freq(arr,n)
print(ans)