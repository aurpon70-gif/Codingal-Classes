# Taking the grades of all 4 subjects
print("Put in your grades in 4 subjects")
Math= int(input("Enter grade Mathematics: "))
Science= int(input("Enter grade for Science: "))
English= int(input("Enter grade for English: "))
History= int(input("Enter grade for History: "))
# Calculating the percentage
Percentage= (Math + Science + English + History) / 400 * 100
# Displaying the percentage
print("Your Grade percentage is:", Percentage)