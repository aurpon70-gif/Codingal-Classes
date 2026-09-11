num = int(input("Enter a number: "))
t = num
numLen = 0

while (t > 0):
    numLen = numLen + 1
    t = int(t / 10)

if numLen>=4:
    numLen = int(numLen/2)
    chk = 0
    while num>0:
        remainder = num % 10
        if chk==numLen:
            midOne = remainder
        elif chk==(numLen-1):
            midTwo = remainder
        num = int(num / 10)
        chk = chk + 1
    prod = midOne*midTwo
    print("\nProduct of the middle digits of the number is: ", prod)

else:
    print("\nThe number is less than 4 digits, so it does not have middle digits.")