n = int(input("Enter a number greater than 1: "))

print("The numbers from {0} to {1} are:".format(n, 1))

for i in range(n, 0, -1):
    print(i)