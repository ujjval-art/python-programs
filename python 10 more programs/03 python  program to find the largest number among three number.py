#importing functions 
import time

#taking input from the user
First_number = float(input("Enter the first number: "))
Second_number = float(input("Enter the first number: "))
Third_number = float(input("Enter the first number: "))

def protototyep(First_number,Second_number,Third_number):
    if(First_number > Second_number and First_number > Third_number):
        print("The first number is greatest")
    elif(Second_number > First_number and Second_number > Third_number):
        print("The second number is greatest")
    elif( Third_number > First_number and Third_number > Second_number):
        print("The Third number is greatest")

time.sleep(3)
print("Thanks for visiting") 