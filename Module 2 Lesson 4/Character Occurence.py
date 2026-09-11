string = input("Enter a word: ")
char = input("Enter a character: ")

i = 0
count = 0

while (i < len(string)):

    if (string[i] == char):
        count = count + 1
    i = i + 1

print(" The amount of times the character appears in your word is: ", count)