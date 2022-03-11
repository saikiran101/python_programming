class Solution:
    def longestConsecutive(self, nums):
        #small=min(nums)
        #empt=[]
        #empt.append(small)
        #print(empt)
        #for i in range(0,len(nums)):
        #    for j in range(0,len(empt)):
        #        if nums[i]==empt[j+1]:
        #            return empt.append(nums[i])
        #return empt
        seen=set(nums)
        visited={}
        def dp(value):
            if value in visited:
                return visited[value]
            lans=1
            if value -1 in seen:
                lans +=dp(value-1)
            visited[value]=lans
            return lans
        ans=0
        for num in seen:
            ans=max(ans,dp(num))
        return ans
s=Solution()
res=s.longestConsecutive([100,20,1,3,2,4])
print(res)

                
