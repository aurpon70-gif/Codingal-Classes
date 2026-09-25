try:
    number = int(input("Enter a number: "))
    print("The number that has been entered is", number)

except ValueError as ex:
    print("Exception:", ex)