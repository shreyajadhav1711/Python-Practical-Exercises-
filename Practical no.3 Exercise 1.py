age = int(input("Enter your age: "))
income = float(input("Enter annual family income: ₹"))

if age < 25 and income < 300000:
    print("Eligible for the scholarship.")
else:
    print("Not eligible for the scholarship.")
