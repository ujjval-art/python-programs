#importing the function
import time

#Taking the input from the user
Number_given_by_user = float(input("Enter the number: "))

#telling user that the work is processing
print("checking the number......")
time.sleep(2)

#checking the numbers

if(Number_given_by_user > 0):
    #if the number is postive
    print("The number is postive")

elif(Number_given_by_user < 0):
    #if the number is  negative
    print("The number is negative")

elif(Number_given_by_user == 0):
    #if the number is zero
    print("The number is zero")

else:
    print("I can't understand please try again")
