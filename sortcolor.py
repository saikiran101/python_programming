class Solution:
    def sortcolor(self,nums):
        red,white,blue=0,0,len(nums)-1
        while white<=blue:
            if nums[white]==0:
                nums[white],nums[red]=nums[red],nums[white]
                white+=1
                red+=1
            elif nums[white]==1:
                white+=1
            else:
                nums[white],nums[blue]=nums[blue],nums[white]
                blue-=1
        return nums
s=Solution()
res=s.sortcolor([2,0,2,1,1,0])
print(res)
