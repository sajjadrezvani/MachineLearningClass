print("Q1")
adequateones=[]
Applicants = {"John": 1983, "Sarah": 1999, "Peter": 1995, "Dane": 2001, "kit": 1979, "Robert": 1980, "Sam": 2010, "Emma": 2000, "Chris": 1899, "Tina": 1991}
values= Applicants.values()
for k,v in Applicants.items():
    if (2023-v)<40 and (2023-v)>20:
        adequateones.append(k)
print(adequateones)

print("##############################################################################################")

applicants = {"John": 1983, "Sarah": 1999, "Peter": 1995, "Dane": 2001, 
              "kit": 1979, "Robert": 1980, "Sam": 2010, "Emma": 2000, 
              "Chris": 1899, "Tina": 1991}

def is_adequate_applicant(birth_year):
    current_year = 2023 # current year
    age = current_year - birth_year
    return 20 <= age <= 40

adequate_applicants = []
for name, birth_year in applicants.items():
    if is_adequate_applicant(birth_year):
        adequate_applicants.append(name)

print("The adequate applicants are:", adequate_applicants)

print("##############################################################################################")

Applicants={"John":1983 , "Sarah":1999 , "Peter":1995 , "Dane":2001 , "Kit":1979 
          , "Robert":1980 , "Sam":2010 , "Emma":2000 , "chris":1899 , "Tina":1991}
Years=list(Applicants.values())
Names=list(Applicants.keys())
for i in range(10):
   if ((2023 - Years[i])<40) and ((2023-Years[i])>20):
      print(Names[i])

print("##############################################################################################")

applicants = {"John": 1983, "Sarah": 1999, "Peter": 1995, "Dane": 2001,
"kit": 1979, "Robert": 1980, "Sam": 2010, "Emma": 2000, "Chris": 1899,
"Tina": 1991}
year=2023

for name in applicants:
    if year-applicants[name]>=20 and year-applicants[name]<=40:
        print(name)

print("##############################################################################################")


Applicants = {"John": 1983, "Sarah": 1999, "Peter": 1995,
              "Dane": 2001, "kit": 1979, "Robert": 1980,
              "Sam": 2010, "Emma": 2000, "Chris": 1899,
              "Tina": 1991}
adequate = {}

items = Applicants.items()
for key, value in items:
    if 1983 <= value <= 2003:
        # print(key,value)
        adequate.update({key: value})

print(f'the applicants are: {Applicants}')
print(f'the adequate applicants are: {adequate}')

print("##############################################################################################")

applicants = {
    "John": 1983, 
    "Sarah": 1999, 
    "Peter": 1995, 
    "Dane": 2001, 
    "kit": 1979, 
    "Robert": 1980, 
    "Sam": 2010, 
    "Emma": 2000, 
    "Chris": 1899, 
    "Tina": 1991
    }

best = []
print(applicants,end="\n\n")
for i in applicants:
    age = 2023 - applicants[i]
    if age > 20 and age < 40:
        best.append(i)
        #print(best.pop())
print(best[0:])

print("##############################################################################################")

Applicants = {"John": 1983, "Sarah": 1999, "Peter": 1995, "Dane": 2001, 
"kit": 1979, "Robert": 1980, "Sam": 2010, "Emma": 2000, "Chris": 1899, 
"Tina": 1991}

names = list(Applicants.keys())
ages = list(Applicants.values())

c = 0
b = 0
c_ages = []
c_names = []
for a in ages:
  if 20 < 2023 - a < 40:
    c_ages.insert(c,a)
    c_names.append(names[b])
    c+= 1
  b += 1

print(c_ages)

print(c_names)

print("##############################################################################################")    

Applicants = {"John": 1983, 
              "Sarah": 1999, 
              "Peter": 1995, 
              "Dane": 2001, 
              "kit": 1979,
              "Robert": 1980,
              "Sam": 2010,
              "Emma": 2000,
              "Chris": 1899, 
              "Tina": 1991
              }

for x,y in Applicants.items():
    if (2023-y)>20 and (2023-y)<40 :
        print(x ,":", y)

print("##############################################################################################")

Applicants = {"John": 1983, "Sarah": 1999, "Peter": 1995, "Dane": 2001, "kit": 1979,
               "Robert": 1980, "Sam": 2010, "Emma": 2000, "Chris": 1899, "Tina": 1991}

adequateList = {}
year = 2023

for name, birthDate in Applicants.items():
    applicantAge = year - birthDate
    if applicantAge >= 20 and applicantAge <= 40:
        adequateList[name] = birthDate

print(adequateList)


print("##############################################################################################")

App = {"John": 1983, "Sarah": 1999, "Peter": 1995, "Dane": 2001, 
"kit": 1979, "Robert": 1980, "Sam": 2010, "Emma": 2000, "Chris": 1899, 
"Tina": 1991}
num={key:(print (key) if 2023-value<40 and 2023-value>20 else print ("not accepted") ) for key,value in App.items()}

print("##############################################################################################")


print("##############################################################################################")



print("##############################################################################################")