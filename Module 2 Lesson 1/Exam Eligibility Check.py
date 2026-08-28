medical_cause = input("Do you have a medical cause? (Y/N): ")

if medical_cause == "Y":
    print("You can take the exam.")
else:
    attendance = int(input("Enter your class attendance: "))

    if attendance >= 75:
        print("You can take the exam.")
    else:
        print("You cannot take the exam.")