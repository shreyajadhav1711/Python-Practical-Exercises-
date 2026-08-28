score = float(input("Enter graduation score (%): "))
backlogs = int(input("Enter number of active backlogs: "))

if score >= 70 and backlogs == 0:
    print("Eligible for placement.")
else:
    print("Not eligible for placement.")
