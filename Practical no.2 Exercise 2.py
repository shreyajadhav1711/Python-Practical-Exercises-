amount = float(input("Enter purchase amount: "))
discount = float(input("Enter discount percentage: "))

discount_amount = amount * discount / 100
final_amount = amount - discount_amount

print("\n----- BILL SUMMARY -----")
print("Purchase Amount =", amount)
print("Discount Amount =", discount_amount)
print("Final Amount =", final_amount)
