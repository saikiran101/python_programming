def disjoint(arr1,arr2):
    for i in range(0,len(arr1)):
        for j in range(0,len(arr2)):
            if arr2[j]==arr1[i]:
                return False
    return True
arr1=[1,2,3,4]      
arr2=[5,3,8,6]
if (disjoint(arr1,arr2)):
    print("disjoint")
else:
    print("not disjoint")