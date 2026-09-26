string = input("Enter a string to reverse: ")

stringR=(" ")

for i in string:
    stringR = i + stringR

print("Your original string is: ", string)
print("The reversed string is: ", stringR)