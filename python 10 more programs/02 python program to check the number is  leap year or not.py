#importing some function
import time

#taking input from the user
Year_given_by_user = int(input("Enter the year: "))

def checkingoftheyear(Year_given_by_user):
    
    if(Year_given_by_user / 4 == 0):
        #if the year is leap year
        print("The year is a leap year.")
    
    else:
        #if the year is not a leap year
        print("The year is not a leap year.")

time.sleep(2)
print("thanks for visiting")