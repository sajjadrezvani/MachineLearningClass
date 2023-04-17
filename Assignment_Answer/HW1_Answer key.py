print("Q1")
adequateones=[]
Applicants = {"John": 1983, "Sarah": 1999, "Peter": 1995, "Dane": 2001, "kit": 1979, "Robert": 1980, "Sam": 2010, "Emma": 2000, "Chris": 1899, "Tina": 1991}
values= Applicants.values()
for k,v in Applicants.items():
    if (2023-v)<40 and (2023-v)>20:
        adequateones.append(k)
print(adequateones)

print("##############################################################################################")
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
print("Q3")

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))

print("##############################################################################################")
print("Q4")

def  Fibonacci(n):
 n_0 = 0  
 n_1 = 1  
 if n < 0:  
    print ("Please enter a valid number")  
 elif n == 0:  
    print(n_0)  
 elif n == 1:
     print(n_1)
 else:  
    count = 0 
    while count <= n:  
        print(n_0)  
        nth = n_0 + n_1  
        n_0 = n_1  
        n_1 = nth  
        count += 1  
          
print(Fibonacci(16))    #for instance 

print("##############################################################################################")
print("Q5")

import math
pos = [0,0]
movement = ("UP 10","DOWN 6","LEFT 8","RIGHT 11") #for instance 
i=0
while i < len(movement):
    move = movement[i]
    s = move.split(" ")
    direction = s[0]
    #print(direction)
    steps = int(s[1])
    #print(steps)
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    i+=1
    
distance = round(math.sqrt(pos[1]**2+pos[0]**2))
print (int(distance))