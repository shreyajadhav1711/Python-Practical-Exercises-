status = input("Enter order status (pending/shipped/delivered): ").lower()

if status == "pending":
    print("Your order is being processed. Please wait.")

elif status == "shipped":
    print("Your order has been shipped and is on the way.")

elif status == "delivered":
    print("Your order has been delivered successfully.")

else:
    print("Invalid order status. Please enter pending, shipped, or delivered.")
