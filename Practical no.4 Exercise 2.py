status = input("Enter climate status (hot/cold/normal): ").lower()

if status == "hot":
    print("Recommendation: Turn on AC")

elif status == "cold":
    print("Recommendation: Activate heater")

elif status == "normal":
    print("Recommendation: Idle")

else:
    print("Invalid climate status")
