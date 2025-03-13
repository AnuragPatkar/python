

""" print("Enter two numbers") #print krne ke liye
a=int(input()) # input in a
b=int(input())
c=a+b
print("Sum is ",c)  """

# this is a single line comment
"""
multi line comment
""" 
#type
x=5
print(type(x)) #type predefined function h ,jo datatype btata h
x=5.6
print(type(x))
x=True
print(type(x))
x="India"
print(type(x))
x=3+4j
print(type(x))
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

import myfile #importing myfile
print(myfile.x) # myfile ke x ko print krne ke liye

import keyword
print("There are ",len(keyword.kwlist),"keywords in python")
print(keyword.kwlist)