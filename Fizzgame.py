#You are going to write a program that automatically prints the solution to the FizzBuzz game.

#Your program should print each number from 1 to 100 in turn.

#When the number is divisible by 3 then instead of printing the number it should print "Fizz".

#`When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
#  `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`
n = int(input().strip())
max_num = 0
count = 0

while n:
        while n&1:
            count += 1
            n>>=1
        max_num = max(count, max_num)
        if not n&1:
            count = 0
            n>>=1

print(max_num)