string="(a+b)"
s=('()')
for i in string:
    if i in s:
        string=string.replace(i,"")  
print(string)

        
