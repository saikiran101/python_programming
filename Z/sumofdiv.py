def sum(start,end,val):
    count=0
    for i in range(start,end+1):
        if i%val==0:
            count+=i
    return count
start=1
end=100
val=7
print(sum(start,end,val))