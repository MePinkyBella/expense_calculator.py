expenses = []

while True:
    expense = input("Enter an expense (or 'done' to finish): ")
    if expense == "done":
        break
    amount = float(input("Enter expense amount: "))
    expenses.append((expense, amount))

total = sum(expense[1] for expense in expenses)

print("Expense report:")
for expense in expenses:
    print(f"{expense[0]}: ${expense[1]:.2f}")
print(f"Total: ${total:.2f}")
