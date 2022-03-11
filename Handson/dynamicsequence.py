def sequence(m,n):
    t=[[0 for i in range(0,m+1)] for i in range(0,m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 and j==0:
                t[i][j]=0
            elif i<j:
                t[i][j]=0
            elif j==1:
                t[i][j]=i
            else:
                t[i][j]=t[i-1][j]+t[i//2][j-1]
    return t[m][n] 
m=10
n=4
res=sequence(m,n)
print(res)