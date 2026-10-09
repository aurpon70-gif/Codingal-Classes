ages=[19, 45, 12, 78]
for age in ages:
    if age < 18:
        print("You are too young, and may not pass.")
        # Exit Now!
        print("And Goodbye!")
        exit()
    else:
        print("You may pass.")