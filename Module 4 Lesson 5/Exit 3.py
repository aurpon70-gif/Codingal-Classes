grades = [85, 92, 76, 60, 98, 54]

for grade in grades:
    if grade < 70:
        print("You have failed, and will not graduate.")
        print("See you next school year!")
        exit()
    else:
        print("Congratulations! You passed and will graduate.")