#input a word
text = str(input("Enter a string: "))

# Putting the string in reverse
revText = text[::-1] 
text = revText

print("Reverse of Given String is:")
print(text)