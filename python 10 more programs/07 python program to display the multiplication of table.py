#importing the modules
import time

#taking the number to take input from the user
n = int(input("Enter the number from the user to print the table"))

#telling the user that the work is processing 
print("The table is printing")
time.sleep(3)

#storing the varibles
i=1

#printing the table
while(i < 11):
    j = n * i
    print("")
    print("",j)