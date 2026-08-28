products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]

item = input("Enter product name to search: ")

if item in products:
    index = products.index(item)
    print("Item found!")
    print("Index location:", index)
else:
    print("Item not found.")
