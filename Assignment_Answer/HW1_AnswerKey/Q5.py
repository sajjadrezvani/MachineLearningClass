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

print("##############################################################################################")

up = int(input('up = '))
down = int(input('down = '))
left = int(input('left = '))
right = int(input('right = '))
row = left - right
column = up - down
result = ((row ** 2)+(column ** 2))**(1/2)
print(f'distance from point (0,0,) is {int(result)}')

print("##############################################################################################")

import math

x, y = 0, 0

moves = ["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]
for move in moves:
    direction, steps = move.split()
    steps = int(steps)
    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps

distance = math.sqrt(x**2 + y**2)

print(round(distance))

print("##############################################################################################")

trace={'up':5,'down':3, 'left':3, 'right':2}

#library for Radical:
import math    #calculating distance using Pythagorean theorem(x^2+y^2=r^2):
r=math.sqrt((trace['up']-trace['down'])**2+(trace['right']-trace['left'])**2)

#rounding distance number and print:
if r-int(r)<int(r)+1-r:
    print(int(r))
else:
    print(int(r)+1)

print("##############################################################################################")


up = int(input('please enter number the steps (move to up): '))
down = int(input('please enter number the steps (move to down): '))
left = int(input('please enter number the steps (move to left): '))
right = int(input('please enter number the steps (move to right): '))

x_distance = abs(up - down)
y_distance = abs(left - right)

x_distance2 = pow(x_distance, 2)
y_distance2 = pow(y_distance, 2)

distance = pow(x_distance2 + y_distance2, 0.5)
distance_round = round(distance)

print(f'the distance from the current position is : {distance_round}')

print("##############################################################################################")

import math

up_tuple=('up',5)
down_tuple=('down',3)
right_tuple=('right',2)
left_tuple=('left',3)

distance=lambda up,down,right,left: int(math.sqrt((up[1]-down[1])**2+(right[1]-left[1])**2))
print(distance(up_tuple,down_tuple,right_tuple,left_tuple))

print("##############################################################################################")

u = int(input('Enter The Number of Ups:'))
d = int(input('Enter The Number of Downs:'))
r = int(input('Enter The Number of Rights:'))
l = int(input('Enter The Number of lefts:'))

pos = [0,0]
pos[1] = u - d
pos[0] = r - l
distance = ((pos[1]**2) + (pos[0]**2))**0.5

dis = int(distance)
print (dis)

print("##############################################################################################")

import math
up = 5
down = 3
left = 3
right = 2

vertical = abs(up-down)
horizental = abs(left-right)

distance =  math.sqrt(pow(vertical,2)+pow(horizental,2))

high = math.ceil(distance)
low = math.floor(distance)

if (high-distance)>(distance-low) :
    rounded_distance = low
elif (high-distance)<(distance-low) :
    rounded_distance = high

print(rounded_distance)

print("##############################################################################################")

x = y = 0  # starting position
for move in ["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]:
    direction, steps = move.split()
    if direction == "UP":
        y += int(steps)
    elif direction == "DOWN":
        y -= int(steps)
    elif direction == "LEFT":
        x -= int(steps)
    elif direction == "RIGHT":
        x += int(steps)

distance = round(((x**2) + (y**2))**0.5)  # calculate distance and round to nearest integer
print(distance)

print("##############################################################################################")

up = int(input('enter the up = '))
down = int(input('enter the down = '))
left = int(input('enter the left = '))
right = int(input('enter the right = '))

row = left - right
colum = up - down
#Pythagoras
result = ((row ** 2) + (colum ** 2)) ** (1/2)

print(f'the distance from poit (0,0,) is {int(result)}')

print("##############################################################################################")

Up = 0
Right = 0
movement = []
for i in range(4):
    n = input("Enter direction and steps like this 'UP 4' ")
    movement.append(n)

for move in movement:
    Type, Step = move.split()
    #Seperate Kind of Movment and number of movement
    Step = int(Step)
    if Type == "UP":
        Up = min(8 ,Up + Step)
        #This min is because we can't get out of Chess Board!
    elif Type == "DOWN":
        Up = max(Up - Step, 0)
        #This max is because we can't get out of Chess Board!
        #print(Up)
    elif Type == "RIGHT":
        Right = min(8 ,Right + Step)
    else:
        Right = max(Right - Step, 0)
        #print(Right)
        
print(round( ( (Up ** 2) + (Right ** 2) ) ** 0.5))

# Pythagorean Theorem and Round the answer to int

print("##############################################################################################")
