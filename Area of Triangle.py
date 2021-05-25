#Python Program to find the area of triangle
a = float(input("Enter the first number"))
b = float(input("Enter the second number"))
c = float(input("Enter the third number"))

#Calculate the semi-perimeter
s = (a+b+c)/2

#Calculate the area
Area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The area of triangle is 0.2f" %Area)
