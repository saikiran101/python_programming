#listOne=[2,5,7,8,9,10]
#listTwo=[5,7,8,2,10,21]
#listthree=list()
#ElementsOne = listOne[1::2]
#ElementTwo = listTwo[0::2]
#print(ElementTwo)
#print(ElementsOne)
#listthree.extend(ElementsOne)
#listthree.extend(ElementTwo)
#print(listthree)
#[5, 8, 10, 5, 8, 10]

#tuple1=(('a',40),('b',86),('c',1),('d',9))
#tuple1=tuple(sorted(list(tuple1),key=lambda x:x[1]))
#print(tuple1)
#(('c', 1), ('d', 9), ('a', 40), ('b', 86))

#list_1=['SAIKIRAN','A','M']
#print([l for l in list_1 if(l[0] == 'A' or l[0] == 'M')])
#['A', 'M']

#list=['p','q','r']
#list+="st"
#print(list)
#['p', 'q', 'r', 's', 't']

#num=19
#while(not(num>>9)):
#    num**=2
#    num=num>>1
#else:
#    num//=2
#print(num)
#8100

#def func(a):
#    if a<=4:
#        return func(a+2)
#    else:
#        return a**2
#print(func(2)+4)
#40

class Person:
    def __init__(self,name,adr,gen):
        self.Name=name
        self.Address=adr
        self.Gender=gen
    def countVowels(self):
        d=0
        for i in self.Name:
            if i.lower() in ['a','e','i','o','u']:
                d+=1
        return d
    def countDigits(self):
        tp=0
        for i in self.Address:
            if i in ['0','1','2','3','4','5','6','7','8','9']:
                tp+=1
        return tp
n=input()
a=input()
g=input()
print(Person(n,a,g))

