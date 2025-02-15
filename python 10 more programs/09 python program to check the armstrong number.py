#importing the function
import time

#taking input from the user
n = int(input("Enter number of digits: "))
The_number = []
for _ in range(n):
    The_number.append(input("Enter the other number: "))

#adding
total = sum(The_number)
print("the answer is: ",total)