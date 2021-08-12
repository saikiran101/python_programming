def f(arr,fn):
    pos=False
    for i in range(len(arr)):
        row= arr[i]
        for j in range(len(row)):
            if fn(row[j]):
                pos=(i,j)
                break
    return pos
print(f([1,2],2))