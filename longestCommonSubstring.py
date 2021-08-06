def lcs(X,Y,m,n):
    Lcsuff=[[0 for k in range(n+1)] for l in range(m+1)]
    result=0
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                Lcsuff[i][j]= 0
            if X[i-1]==Y[j-1]:
                Lcsuff[i][j]=Lcsuff[i-1][j-1]+1
                result=max(result,Lcsuff[i][j])
            else:
                Lcsuff[i][j]=0
    return result
X="saikiran"
Y="saiadjc"

m=len(X)
n=len(Y)
print("longest common substring",lcs(X, Y, m, n))