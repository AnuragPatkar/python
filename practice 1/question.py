""" #1.Write a python script to calculate area of a rectangle
length=int(input("Enter length: "))
width=int(input("Enter width: "))

area = length * width
print("Area of rectangle:", area) """

"""#2.Write a python script to calculate simple interest
p=int(input("Enter Principle Amount "))
r=float(input("Enter Rate of interest "))
t=float(input("Enter Time "))
print("Simple interest is ",p*r*t/100)
"""

""" #3.Write a python script to remove the last digit form a given number
x=int(input("Enter a number"))
print(x//10)
 """

""" #4.Write a python script to swap data of two variables
x=5
y=6
z=x
x=y
y=z
print(x,y) """

""" #5.Write a python script to check whether a given number is divisible by 5 or not
x=int(input("Enter a number"))
if x%5==0:
    print("Divisible by 5")
else: 
    print("Not Divisible by 5") """

""" #6.write a python script to print two given words in dictionary order
x="Anurag"
y="Akash"
if x>y:
    print(y,x)
else:
    print(x,y) """

""" #7.write a python script to check whether a given number is three digit number or not
x=int(input("Enter a number "))
if x>99 and x<1000:
    print(x,"is three digit number")
else:
    print(x,"is not a three digit number")
 """

""" #8.write a python script to check whether a given year is leap year or not
x=int(input("Enter year "))
if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
    print(x, "is a Leap year")
else:
    print(x, "is not a Leap year") """

""" #9.check given number positive or negative or zero
x=int(input("Enter a number "))
if x>0:
    print("positive")
elif x==0:
    print("Zero")
else:
    print("Negative") """

""" #10.Write a python script to accept a complex number and display the greater number between real and imaginary part
x=complex(input("Enter a Complex number "))
real=x.real
imag=x.imag

if imag>real:
    print(imag)
else:
    print(real) """