lower = int(input("Enter the first number: "))  # Get the first number
upper = int(input("Enter the second number: "))  # Get the second number

print("Prime numbers between", lower, "and", upper, "are:")

num = lower
while (num <= upper):
    if (num > 1):  # Check if num is greater than 1
        i = 2
        is_prime = True

        while (i < num):  # Check divisibility from 2 to num-1
            if (num % i == 0):  # If divisible, it's not prime
                is_prime = False
                break
            i += 1

        if (is_prime):  # If prime, print the number
            print(num)

    num += 1  # Move to the next number
