days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
hours = ["9-10", "10-11", "11-12", "12-1", "1-2"]
schedule = [
    ["Math", "English", "Science", "History", "Computer"],
    ["English", "Math", "Computer", "Science", "History"],
    ["Science", "History", "Math", "English", "Computer"],
    ["Computer", "Science", "English", "Math", "History"],
    ["History", "Computer", "Science", "Math", "English"]
]
def display_schedule():
    print("\nClass Schedule:")
    print("Hour\t", end="")
    for day in days:
        print(day, "\t", end="")
    print()
    for i in range(len(hours)):
        print(hours[i], "\t", end="")
        for j in range(len(days)):
            print(schedule[i][j], "\t", end="")
        print()
display_schedule()
day = int(input("\nEnter day number (1-5): "))
hour = int(input("Enter hour slot (1-5): "))
if 1 <= day <= 5 and 1 <= hour <= 5:
    new_subject = input("Enter the new subject/topic: ")
    schedule[hour - 1][day - 1] = new_subject
    print("\nSchedule updated successfully!")
    display_schedule()
else:
    print("Invalid day or hour slot.")
