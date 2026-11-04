# 1 condition - if statement
# 1 condition, 2 outputs - if-else statement
# 2 conditions, 3 outputs - if-elif-else statement

# Topic 1: Conditional Statements 
# Program 1: Smart Canteen Discount System
# Topic: if, elif, else, comparison operators, and logical thinking.
# Real-World Scenario
# Imagine a college canteen where students receive discounts based 
# on their total bill.

# The canteen follows these rules:
# - If the bill is Rs. 3,000 or more, the student receives a 
# 20% discount.
# - If the bill is Rs. 2,000 or more but less than Rs. 3,000, 
# the student receives a 10% discount.
# - If the bill is Rs. 1,000 or more but less than Rs. 2,000, 
# the student receives a 5% discount.
# - If the bill is less than Rs. 1,000, no discount is provided.
# - The program must display the original bill, discount amount,
# and final payable amount.

print("===== SMART CANTEEN =====")
bill_amount = float(input("Enter your total bill amount (Rs.): "))

# Challenge Feature 1: Validate if the bill is less than or equal to zero
if bill_amount <= 0:
    print("Error: Invalid bill amount. Please enter a value greater than zero.")
else:
    # Challenge Feature 2: Ask about membership card status
    has_membership = input("Do you have a membership card? (yes/no): ").strip().lower()

    if bill_amount >= 3000:
        discount_rate = 20
    elif bill_amount >= 2000:
        discount_rate = 10
    elif bill_amount >= 1000:
        discount_rate = 5
    else:
        discount_rate = 0

    # Challenge Feature 2: Add an extra 5% if membership card
    if has_membership == "yes":
        discount_rate += 5

    discount_amount = bill_amount * discount_rate / 100
    final_amount = bill_amount - discount_amount

    print("\n===== BILL SUMMARY =====")
    print(f"Original Bill: Rs. {bill_amount:.2f}")
    # Added this line so the membership response actually shows up in the output terminal
    print(f"Membership Card: {has_membership.capitalize()}")
    print(f"Total Discount Rate: {discount_rate}%")
    print(f"Discount Amount: Rs. {discount_amount:.2f}")
    print(f"Final Payable: Rs. {final_amount:.2f}")

    # Challenge Feature 3: Display savings message if a discount applies
    if discount_amount > 0:
        print(f"Congratulations! You saved Rs. {discount_amount:.2f}")