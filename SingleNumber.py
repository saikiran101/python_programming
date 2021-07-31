class Solution:
    def singleNumber(self, nums):
        result=[]
        for i in nums:
            if i not in result:
                result.append(i)
            else:
                result.remove(i)
        return result.pop()

s=Solution()
res=s.singleNumber([2,2,1])
print(res)