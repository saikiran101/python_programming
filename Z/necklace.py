from itertools import cycle
S='abcd'
c=cycle(S)
res=[]
for i in range(len(S)):
    st = ''
    count = 0
    for j in (c):
        if count == len(S):
            break
        st +=j
        count +=1
    res.append(st)
    res.append(st)
print(res)
final=set(res)
print(len(final))