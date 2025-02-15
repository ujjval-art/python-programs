#python program to find the area of triangle

#importing the functions
import time

#taking the input from the user
Base_of_the_triangle = float(input("Enter the base of the triangle: "))
Height_of_the_triangle = float(input("Enter the height of the triangle: "))

#Calculating the area

area_of_the_triangle = 1/2 * Base_of_the_triangle * Height_of_the_triangle

print("Caclulating the area....")
time.sleep(2)

print("The area of the triangle is: ",area_of_the_triangle)