a = 10
b = 20
c = -5

print(not  (a == b))

print(not (b == c))

a = "math"
b = "fun"

if not (a == b):
    print("a and b are not equal")

a = 4
b = 5

if not ((a == 1) == (b == 5)):
    print("This is a line of code")

a = int(input("Enter a number: "))

if not (a % 2 == 0):
    print(a, "is odd")