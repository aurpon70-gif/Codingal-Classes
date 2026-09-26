starting_n= int(input("Enter a number to start from: "))
ending_n= int(input("Enter a number to end at: "))

if starting_n > ending_n:
    print("The numbers from {0} to {1} are:".format(starting_n, ending_n))

    for i in range(starting_n, ending_n, -2):
        print(i)
else:
    print("Please put a starting number that is larger than the ending number.")
               