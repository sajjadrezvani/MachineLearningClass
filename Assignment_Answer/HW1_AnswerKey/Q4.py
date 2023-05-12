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

student_id_number = input('enter your student ID number : ')
N=int(student_id_number[-2])
N = N * N
n1,n2 = 0,1
Fibonacci =[str(n1)]
while N-1:
    Fibonacci.append(str(n2))
    n1,n2 = n2, n1+n2
    N = N - 1
final_Fibonacci = " , ".join(Fibonacci)
print(final_Fibonacci)

print("##############################################################################################")

def fibunachi(a):
  fib =[0,1]
  for i in range(2, a+1):
    fib.append(fib[i-2]+fib[i-1])
  return fib

print(fibunachi(9))

print("##############################################################################################")

print ("Enter your id = ")
id=input ()
num=int (id[6])
num1=num*num
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num1):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()

print("##############################################################################################")



print("##############################################################################################")



print("##############################################################################################")



print("##############################################################################################")