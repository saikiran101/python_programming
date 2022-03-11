from datetime import datetime
first=datetime.now()
n=int(input("enetr the interger"))
type=[]
for i in range(0,n):
    type.append(int(input("typearray")))
power=[]
for i in range(0,n):
    power.append(int(input("powerArray")))
print("type",type)
print("power",power)
caseResults=[]
totalResult=1
for i in range(0,n):
    if i==0:
        caseResults.append(power[i])
    else:
        if type[i-1]==1:
            caseResults.append(caseResults[i-1]+power[i]*2)
        else:
            caseResults.append((caseResults[i-1]+power[i]))
    totalResult =totalResult*caseResults[i]
print(caseResults)
print(totalResult)
last=datetime.now()
print(last-first)
