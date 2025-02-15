#importing the functions
import time

#taking the input from the user
num = float(input("Enter the number: "))

#Showing the user that work is in processs
print("checking the number.........")
time.sleep(2)

#checking the number

if(num == 0):
    #if number is zero then:
    print("the number is zero ")

elif(num > 0):
    #if the number is postive then:
    print("the number is postive")

elif(num < 0):
    #if the number is negative then: 
    print("the number is negative")

else:
    #cant understand
    print("try again cant understand")

time.sleep(2)
print('''Thank you for comming''')