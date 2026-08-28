grades = [75, 80, 65, 90, 85]

print("Original Grades:", grades)

index = int(input("Enter index position to change (0-4): "))
new_grade = int(input("Enter new grade: "))

grades[index] = new_grade

print("Corrected Grades:", grades)
