def rec(n):
    if n==0:
        return 0
    else:
        rec(n-1)
        print(n)
rec(5)