c=int(input())
java=int(input())
python=int(input())
result=(c+java+python)/3
if c>=35 and java>=35 and python>=35:
    if result>=90:
        print("outstanding")
    elif result<=90 and result>=70:
        print("excellent")
    elif result<=70 and result>=50:
        print("good")
    else:
        print("pass")
else:
    print("fail")