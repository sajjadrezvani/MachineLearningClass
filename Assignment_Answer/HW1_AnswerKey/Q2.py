print("Q2")

s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("\n")
print("Sum is: ", s)

print("##############################################################################################")

number=int(input("Enter the desired number:"))
s=0
show=''
for i in range(1, number+1):
    s = s + i
    if i != number:
         show = show + (str(i) + '+')
    else:
         show = show + (str(i) + '=')
print(show,s)

print("##############################################################################################")

summation = 0
number = int(input("input ur number: "))
for i in range(1,number+1) :
    summation += i
    if i==number :
        print(i,end=" ")
    else:
        print(i,end=" + ")
print(f"= {summation}")

print("##############################################################################################")

import numpy as np
n = int(input('Enter The Number:'))

e = np.arange(n+1)
print(e.sum())

print("##############################################################################################")

a=input("Please enter a number : ")
a=int(a)
print(a*(a+1)/2)

print("##############################################################################################")



print("##############################################################################################")



print("##############################################################################################")