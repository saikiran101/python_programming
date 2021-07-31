def findS(arr,row):
    hm=dict()
    for i in range(row):
        f=arr[i],arr[0]
        s=arr[i],arr[1]
        if (s in hm.keys() and hm[s] == f):
            print("symmentrics",s,f)
        else:
            print("there is no symmentric pairs")
arr=[[5,7],[7,5],[4,5],[5,4]]
findS(arr,int(input()))