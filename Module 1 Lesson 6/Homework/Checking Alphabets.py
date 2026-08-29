# Take character input from the user
ch = input("Enter any character: ")

# Check if the character is an alphabet
if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
    print(ch, "is an alphabet.")
else:
    print(ch, "is not an alphabet.")