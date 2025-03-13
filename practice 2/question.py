""" #1.Write a python script to print first 10 odd natural numbers.
x=10
i=1
while i<=x:
    print(2*i-1)
    i+=1
     """

""" #2.Write a Python script to print first N even natural numbers.
N=int(input("Enter a number "))
i=1
while i<=N:
    print(2*i)
    i+=1 """

""" #3.Write a Python script to print first 10 odd natural numbers in reverse order.
x=10
while x>0:
    print(2*x-1)
    x-=1
     """

""" #4.Write a Python script to print squares of first N natural numbers.
N=int(input("Enter a number "))
i=1
while i<=N:
    print(i*i)
    i+=1 """

""" #5.Write a pythen script to calculate Sumof first N natural numbers.
N=int(input("Enter a number "))
s=0
i=1
while i<=N:
    s+=i
    i+=1
print(s) """

""" #6.Write a Python script to calculate factorial of a number.
N=int(input("Enter a number "))
f=1
while N>0:
    f*=N
    N-=1
print(f) """

""" #7.Write a Python script to count digits in a given number.
N=int(input("Enter a number "))
c=0
while N>0:
    N=N//10
    c+=1
print(c) """

""" #8.Write a Python script to calculate sum of the digits of a given number.
N=int(input("Enter a number "))
s=0
while N>0:
    s+=N%10
    N=N//10
print(s)
 """

""" #9.Write a python script to check whither a given number is Prime or not.
x=int(input("Enter a number "))
i=2
while(i<x):
    if x%i==0:
     break
    i+=1
if x==i:
   print(x,"is prime number")
else:
   print(x,"is not a prime number") """

""" #10.Write a Python script to calculate LCM of twe numbers.
x=int(input("Enter First Number "))
y=int(input("Enter Second Number "))
max = x if x > y else y
while max<= x*y:
    if max%x==0 and max%y==0:
        print("Lcm is ",max)
        break
    max+=1
 """
""" import math

# Function to calculate LCM
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

print("LCM is:", lcm(x, y)) """

