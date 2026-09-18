def add(P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    return P / Q
def modulus(P, Q):
    return P % Q

print ("Please select an operation: ")
print ("A. Addition")
print ("B. Subtraction")
print ("C. Multiplication")
print ("D. Division")
print ("E. Modulus")

choice = input ("Enter you choice (A/B/C/D/E): ")

num_1 = int(input ("Enter your first number: "))
num_2 = int(input ("Enter your second number: "))

if choice == 'A':
    print (num_1, "+", num_2, "=", add(num_1, num_2))
if choice == 'B':
    print (num_1, "-", num_2, "=", subtract(num_1, num_2))
if choice == 'C':
    print (num_1, "*", num_2, "=", multiply(num_1, num_2))
if choice == 'D':
    print (num_1, "/", num_2, "=", divide(num_1, num_2))
if choice == 'E':
    print (num_1, "%", num_2, "=", modulus(num_1, num_2))
else:
    print ("This is an invalid input.")
