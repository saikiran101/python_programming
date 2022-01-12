import sys
l="bale"
s="elbz"
if len(l)!=len(s):
    print("not an anagram")
    sys.exit()
l=sorted(l)
s=sorted(s)
if l == s:
    print("anagram")
else:
    print("not an anagram")