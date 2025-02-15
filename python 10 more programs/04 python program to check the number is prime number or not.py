#importing function
import time

#declaring varible
boolean = 0

#taking input from the user
Number_for_checking = float(input("Enter the number: "))

#storing varibles
i = Number_for_checking
one = 1
print("10% work is done")
time.sleep(2)

#calculating
while(one < i):
    if(i%one==0):
        boolean=1
        break
    else:
        boolean=0
    
    one = one + 1
print("90% percent work done")
time.sleep(2)
#checking
if(boolean == 1):
    print("The number is  prime number.")
else:
    print("The number is not prime number")