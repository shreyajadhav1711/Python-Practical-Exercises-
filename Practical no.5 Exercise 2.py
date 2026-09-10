food = 0
travel = 0
shopping = 0

n = int(input("Enter number of expenses: "))

for i in range(n):
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    if category == "Food":
        food = food + amount
    elif category == "Travel":
        travel = travel + amount
    elif category == "Shopping":
        shopping = shopping + amount

print("\nMonthly Expense")
print("Food =", food)
print("Travel =", travel)
print("Shopping =", shopping)
print("Total =", food + travel + shopping)
