print("Basic - Print all integers from 0 to 150.")
from operator import imod


for i in range(151):
    print(i)

print("Multiples of Five - Print all the multiples of 5 from 5 to 1,000")

for i in range(5,1001,5):
    print(i)

print("or another way of doing Multiples of Five ")
for i in range(5,1001):
    if i%5==0:
        print(i)

print("or another way of doing Multiples of Five ")
for i in range(1000):
    mul=i*5
    if mul>1000:
        break
    else:
        print(mul)

print('Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".')
for i in range(101):
    if i%10==0:
        print("Coding Dojo")
    elif i%5==0:
        print("Coding")
    else: print(i)

print("Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.")

sum = 0
for i in range(1,500000,2):
    sum+=i

print(sum)

print("Countdown by Fours - Print positive numbers starting at 2018, counting down by fours")

for i in range(2018,-1,-4):
    print(i)

print("Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)")

def multi_mult(lowN,highN,mult):
    for i in range(lowN,highN):
        if i%mult==0:
            print(i)

multi_mult(2,875,17)








