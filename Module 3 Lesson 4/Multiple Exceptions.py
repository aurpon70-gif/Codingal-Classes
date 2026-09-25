try:
    num1, num2 = eval(input("Enter two numbers seperated by a comma : "))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("You can't divide anything by 0!")

except SyntaxError:
    print("You're missing the comma.")

except:
    print("Input is not valid")

else:
    print("No exceptions")

finally:
    print("This code will be executed no matter what!")