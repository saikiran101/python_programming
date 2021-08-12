class Solution:
    def subarray(self,nums,k):
        if k<=1: return 0
        prod =1
        ans=left=0
        for right,val in enumerate(nums):
            prod*=val
            while prod>=k:
                prod/=nums[left]
                left+=1
            ans+= right-left+1
        return ans
res=Solution()
s=res.subarray([10,5,2,6],100)
print(s)
