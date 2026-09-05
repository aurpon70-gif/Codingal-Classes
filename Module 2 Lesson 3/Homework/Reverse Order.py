# Take input from the user
num = int(input("Enter a number: "))

# Initialize count variable
count = 0

temp = abs(num)

if temp == 0:
    count = 1
else:
    while temp > 0:
        temp = temp // 10
        count += 1

print(f"Total digits: {count}")