#Imoporting function
import time

#taking the input from the user
Number = float(input("Enter the number: "))

#saying to user that the work is processing
print("Checking the number is even or odd........")
time.sleep(2)

if(Number / 2 == 0):
    #means the number is even
    print("The number is even")

elif(Number / 2 != 0):
    #means the number is odd
    print("The number is odd")

else:
    print("I can't understand please try again")