#importing the module
import time

#taking the number
Number_given_by_user = int(input("Enter the number: "))

#showing the user that the work is processing
print("Calculating the factorial..........")
time.sleep(3)

#storing the variable
n = Number_given_by_user
j = 1

#checking if the number is zero
if n == 0:
    print("The factorial is: 1")
else:
    while n > 1:
        j *= n
        n -= 1
    print("The factorial is:", j)        