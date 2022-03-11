nums=[100,20,1,2,3,4]
small=min(nums)
empt=[]
empt.append(small)
print(empt)
for i in range(0,len(nums)): 
    for j in range(len(empt)):   
        if nums[i]==empt[j] +1:
            empt.append(nums[j])
            
print(len(empt))