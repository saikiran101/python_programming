class Solution:
    def maximumsubarray(self,nums):
        newNum=maxprofit=nums[0]
        for i in range(1,len(nums)):
            newNum=max(nums[i],nums[i]+newNum)
            maxprofit=max(newNum,maxprofit)
        return maxprofit
s=Solution()
result=s.maximumsubarray([-2,1,4])
print(result)