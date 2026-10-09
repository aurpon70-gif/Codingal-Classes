test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print("Test Dictionary:")
print(test_dict)

user_value = int(input("\nEnter the number assigned to a word you want to check the frequency of: "))

frequency = list(test_dict.values()).count(user_value)

print(f"The frequency of the value {user_value} is: {frequency}")