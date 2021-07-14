class Solution:
    def missingNumber(self, nums) -> int:
        num=sorted(nums)
        size= len(num)+1
        for i in range(size):
            if i not in num:
                return i

s=Solution()
res=s.missingNumber([0,3,1])
print(res)