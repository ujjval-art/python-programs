# Input the number from the user
number = int(input("Enter a number: "))

# Initialize a variable to store the sum of digits
digit_sum = 0

# Loop through each digit of the number
while number > 0:
    # Extract the last digit of the number
    last_digit = number % 10
    
    # Add the last digit to the sum
    digit_sum += last_digit
    
    # Remove the last digit from the number
    number = number // 10

# Print the sum of the digits
print("The sum of the digits is:", digit_sum)
