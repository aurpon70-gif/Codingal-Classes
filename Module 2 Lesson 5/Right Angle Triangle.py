print("We are going to create a right angle triangle with asterisks.")
n = int(input("Enter the number of rows for the triangle: "))

for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()