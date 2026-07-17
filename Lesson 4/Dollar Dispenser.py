# Deciding the amount of money to deposit
Amount= int(input("Enter the amount of money you would like to deposit: "))
# Calculating the number of each denomination
Check1= Amount // 100
Check2= (Amount%100) // 50
Check3= ((Amount%100)%50) // 10
# Displaying the amount of each check
print("The amount of 100-dollar checks is:", Check1)
print("The amount of 50-dollar checks is:", Check2)
print("The amount of 10-dollar checks is:", Check3)

