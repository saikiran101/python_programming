#Minimum
#v1=[5,7,9,10]
#v2=[2,9,11,3]
#ass
#v1.sort()
#des
#v2.sort(reverse=True)
#res=0
#for i in range(0,len(v1)):
#    res+=v1[i]*v2[i]
#print(res)

#or
#Maximum
v1=[5,7,9,10]
v2=[2,9,11,3]
#ass
v1.sort()
#ass
v2.sort()
res=0
for i in range(0,len(v1)):
    res+=v1[i]*v2[i]
print(res)
