#importing the function
import time 

#taking the number
taking_the_number_from_the_user = int(input("Enter the number: "))

#storing the variable
T = taking_the_number_from_the_user
j = 0
k = 1

#telling the user that the work is processing
print("The work is processing........")
time.sleep(2)

#printing the zero and one
print(" ", j)
print(" ", k)

#calculating the work
m = 2  # Since we already printed the first two numbers
while (m < T):
    next_term = j + k
    print(" ", next_term)

    #updating values
    j = k
    k = next_term

    #increment
    m = m + 1

print("Thanks for coming")
