def segregate(arr, n):
    z, o = 0, n - 1
    while z <= o:
        if arr[z] == 1:
            arr[z], arr[o] = arr[o], arr[z] 
            o -= 1
        elif arr[o] == 0:
            arr[o], arr[z] = arr[z], arr[o]
            z += 1
        else:
            o -= 1
            z += 1
    return arr
res = segregate([1, 1, 1, 1, 0], 5)
print(res)