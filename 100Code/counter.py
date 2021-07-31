from collections import Counter
arr=[int(input()) for _ in range(int(input()))]
count=Counter(arr)
print(count)
for key, value in count.items():
    print("{} occurs in {} time".format(key,value))