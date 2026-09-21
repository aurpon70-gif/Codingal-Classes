def calculate_due_amount(bill_amount, amount_paid):
    return amount_paid - bill_amount

total_bill = 2.50
amount_paid = 4.00

change_due = calculate_due_amount(total_bill, amount_paid)

print(f"The shopkeeper should return: ${change_due:.2f}")