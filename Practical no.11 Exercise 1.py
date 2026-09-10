seats = [
    ["O", "O", "O"],
    ["O", "O", "O"],
    ["O", "O", "O"]
]
print("Current Seating Arrangement:")
for row in seats:
    print(row)
row = int(input("Enter row number (1-3): "))
column = int(input("Enter column number (1-3): "))
if 1 <= row <= 3 and 1 <= column <= 3:
    if seats[row - 1][column - 1] == "O":
        seats[row - 1][column - 1] = "X"
        print("Seat reserved successfully!")
    else:
        print("Sorry, this seat is already reserved.")
    print("\nUpdated Seating Arrangement:")
    for r in seats:
        print(r)
else:
    print("Invalid row or column.")
