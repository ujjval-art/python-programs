# Input the number to check
number =int(input("Enter a number: "))

# Check if the number is less than or equal to 1 (not prime)
if number <= 1:

    print(f"{number} is not a prime number.")
else:
    # Assume the number is prime initially
    is_prime = True
    
    # Check divisibility from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        # If the number is divisible by i, it's not prime
        if number % i == 0:
            is_prime = False
            break  # Exit the loop as we've found it's not prime

    # Print the result based on whether the number is prime or not
    if is_prime:
        {
            print(f"{number} is a prime number.")
        }
    else:
        {
            print(f"{number} is not a prime number.")
        }
