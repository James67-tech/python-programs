import math

#Area of a circle

radius = float(input("Enter the radius of the circle in cm : "))
area = round(math.pi * pow(radius,2),2)
print("Area of the circle to 2 decimal places is : ",area, "cm^2")  

#Find hypotenuse of a right angle triangle

side_a = float(input("Enter the length of side a in cm : "))
side_b = float(input("Enter the length of side b in cm : "))
hypotenuse = round(math.hypot(side_a, side_b),2)
print("The hypotenuse of the right angle triangle is : ",hypotenuse, "cm")    