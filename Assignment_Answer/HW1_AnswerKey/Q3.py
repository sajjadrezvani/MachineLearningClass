print("Q3")

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))

print("##############################################################################################")

for i in range(2000,3201):
    if i % 7==0 and i%5 != 0 :
        print(i,end=",")

print("##############################################################################################")

list = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        i = str(i) # str mikonim ke az join estefade konim va [] ro hazf konim faghat jomleha bemune
        list.append(i)

# print(list)

separate = ', '
print(separate.join(list))

print("##############################################################################################")

import numpy as np
d = np.arange(3200)
d = d[2000:3200]

res = []
for i in d:
  if i%7 == 0:
    if i%5 != 0:
      res.append(i)

print(res)

print("##############################################################################################")

numbers = []
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        numbers.append(num)

print(", ".join(str(num) for num in numbers))

print("##############################################################################################")

import numpy as np
st = 2000
end = 3200
num = np.arange(2002,3200,7)
num= num[(num % 5 != 0)]
print(num)

print("##############################################################################################")



print("##############################################################################################")