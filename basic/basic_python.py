

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

print("Even" if int(input("Enter a number"))%2==0 else "Odd") 