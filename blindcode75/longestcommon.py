class Solution:
    def longestCommonSubsequence(self, text1, text2):
        #stack=""
        #for i in text1:
        #    for j in text2:
        #        if i==j:
        #            stack+=str(i)
        #return len(stack)
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j]=1+ dp[1+i][j+1]
                else:
                    dp[i][j]=max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]
s=Solution()
res=s.longestCommonSubsequence("abc","abc")
print(res)