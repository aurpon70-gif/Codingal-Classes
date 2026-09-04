# Take inputs for base number and exponent (n)
base = int(input("Enter the base number: "))
exponent = int(input("Enter the power (n): "))

# Initialize result to 1 (since multiplying by 1 changes nothing)
result = 1

# Use a for loop to multiply the base 'exponent' times
for _ in range(exponent):
    result *= base

# Display the calculated power
print(f"{base} raised to the power of {exponent} is: {result}")