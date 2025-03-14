

""" print("Enter two numbers") #print krne ke liye
a=int(input()) # input in a
b=int(input())
c=a+b
print("Sum is ",c)  """

# this is a single line comment
"""
multi line comment
""" 
""" #type
x=5
print(type(x)) #type predefined function h ,jo datatype btata h
x=5.6
print(type(x))
x=True
print(type(x))
x="India"
print(type(x))
x=3+4j
print(type(x)) """
#char & double is not in python
#int, float, complex, bool, str is class in python
#address is called id in python
#garbage block  jise koi refer nhi kr rha h
#python is case sensitive
#python is dynamically typed language
#python is interpreted language
#python is platform independent
#python is open source
#python m auto memory management hoti h
#python m dynamically object create hota h
#object= object is something which can store data and has some methods to handle data

""" import myfile #importing myfile
print(myfile.x) # myfile ke x ko print krne ke liye

import keyword
print("There are ",len(keyword.kwlist),"keywords in python")
print(keyword.kwlist) """

#opetaors
#1. Arithmetic operators (+,-,*,/,%,//,**)
#2. Assignment operators (=,+=,-=,*=,/=,%=,//=,**=)
#3. Comparison operators (==,!=,<,>,<=,>=)
#4. Logical operators (and,or,not)
#5. Bitwise operators (&,|,^,~,<<,>>)
#6. Identity operators (is,is not) #is is used to check the address of two variables
#7. Membership operators (in,not in) #in is used to check the value in the list or not  #not in is used to check the value is not in the list
#8. Ternary operators (a if condition else b) #if condition is true then a otherwise b  
#no ++ or -- operator in python

""" #write a program to check whether a given number is positive or non positive
x=int(input("Enter a number"))
if x>0:
    print("Positive")
if x<=0:
    print("Non Positive")
print("Thank you") """

""" #write a program to check whether a given number is even or odd
x=int(input("Enter a number"))
if x%2==0:
    print("Even")
else:
    print("Odd") """

""" #if elif else
#write a program to check whether a given number is positive or negative or zero"
x=int(input("Enter a number"))
if x>0:
    print("Positive")
elif x<0:
    print("Negative")
else:
    print("Zero") """

#single line if else

#print("Even" if int(input("Enter a number"))%2==0 else "Odd") 

#loop
""" #write a program to print mysirg on screen 5 times
x=5
while x>0:
    print("MySirg")
    x=x-1; """

""" #write a program to print first N natural numberc
x=int(input("Enter value of N "))
i=1
while i<=x:
    print(i)
    i+=1
 """

""" #write a program to calculate sum of N natural Number
x=int(input("Enter value of N "))
s=0
while x>0:
    s+=x
    x-=1
print(s)
     """

""" #check prime number or not
x=int(input("Enter a number "))
i=2
while(i<x):
    if x%i==0:
     break
    i+=1
if x==i:
   print(x,"is prime number")
else:
   print(x,"is not a prime number")
 """
""" #for loop
x="MySirg"
for i in x:
    print(i,ord(i)) """

""" # range  
r=range(1,10,1)
print(r)
for i in r:
    print(i) """

""" #write a program to print N natural numbers
x=int(input("Enter a number "))
for i in range(1,x+1):
    print(i,end=' ') """

""" #write a program to print squre of first N natural number
x=int(input("Enter a number "))
for i in range(1,x+1):
    print(i**2,end=' ') """

#list
l1=[10,20,30]
print(type(l1))
l2=[10,5.5,30,"anu"]
print(type(l2))
print(l1)
print(l2)
print(l1[0],l1[1])
print(l1[-3],l1[-2]) #negative indexing
for i in l2:
    print(i,end=' ')
print()  # To move to the next line after the loop
#delete
del l2[3]
for i in l2:
    print(i,end=' ')
print()  # To move to the next line after the loop
#edit
l2[0]=50
for i in l2:
    print(i,end=' ')
print()  # To move to the next line after the loop
#append
l2.append(70)
for i in l2:
    print(i,end=' ')
print()
#insert
l2.insert(2,120)
for i in l2:
    print(i,end=' ')
print()

