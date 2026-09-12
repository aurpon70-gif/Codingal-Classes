rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    # Print spaces (decreasing count)
    print(" " * (rows - i), end="")
    # Print stars (increasing count)
    print("*" * i)