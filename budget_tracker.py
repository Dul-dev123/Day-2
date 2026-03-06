# Part 3: Budget Tracker - Task 01 & 02
print("--- Simple Budget Tracker ---")

# Get the initial budget
total_budget = float(input("Enter your total monthly budget (LKR): "))

# Get 3 expenses
exp1 = float(input("Enter expense 1: "))
exp2 = float(input("Enter expense 2: "))
exp3 = float(input("Enter expense 3: "))

# Calculate remaining balance
remaining = total_budget - (exp1 + exp2 + exp3)

print(f"\nTotal Budget: {total_budget}")
print(f"Remaining Balance: {remaining}")

# Task 02: Low funds warning
if remaining < 500:
    print("⚠️ Warning: Low Funds!")
else:
    print("You're doing great with your budget!")