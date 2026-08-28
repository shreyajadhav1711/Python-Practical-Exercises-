subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

total = subject1 + subject2 + subject3

average = total / 3

print("\n----- Student Scorecard -----")
print("Subject 1:", subject1)
print("Subject 2:", subject2)
print("Subject 3:", subject3)
print("Total Marks:", total)
print("Average:", round(average, 2))
