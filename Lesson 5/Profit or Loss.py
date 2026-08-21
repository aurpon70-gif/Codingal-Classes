actual_cost = float(input("Enter the actual product price: "))
sale_cost = float(input("Enter the amount that the product is sold for: "))

if (sale_cost > actual_cost):
    amount = sale_amount = actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("You have not made any profit.")