try:
    user_input = input("Enter your age: ")
    
    age = int(user_input)
    
    if age % 2 == 0:
        print(f"The age you entered ({age}) is an even number.")
    else:
        print(f"The age you entered ({age}) is an odd number.")
        

except ValueError:
    # This block catches any invalid entries (decimals, alphabets, or special characters)
    print("Value Error: Please enter a valid whole number for your age.")