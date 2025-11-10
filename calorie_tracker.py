from datetime import datetime

print("Good evening sir/ma'am this is a mini CLI(Command Line Interface) tool that will track the total calories consumed by you")

count = int(input("Enter number of meals you want to enter:  "))

Meal_List = []
Calorie_Amount = []

for i in range(count):
    Name = input("Enter meal name:  ")
    Meal_List.append(Name)
    Amount = int(input("Enter calorie of the meal:  "))
    Calorie_Amount.append(Amount)

print("\nMeals entered:")
for w in range(len(Meal_List)):
    print(Meal_List[w], "\t", Calorie_Amount[w])

total_calories = sum(Calorie_Amount)
print("Sum:", "\t", total_calories)

average_calories = total_calories / len(Calorie_Amount)
print("Your avg calorie intake is:", "\t", average_calories)

limit = float(input("Enter your daily calorie limit: "))

if total_calories > limit:
    status = "WARNING: you have exceeded your daily limit"
else:
    status = "SUCCESS: you are within the limit"

print(status)

save = input("\nWould you like to save this report? (yes/no): ").strip().lower()

if save == "yes":
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "myfile.txt"
    with open(filename, "w") as f:
        f.write("Daily Calorie Tracker Report\n")
        f.write(f"Timestamp: {timestamp}\n\n")
        f.write("Meals Entered:\n")
        for meal, cal in zip(Meal_List, Calorie_Amount):
            f.write(f"{meal}: {cal} calories\n")
        f.write(f"\nTotal calorie intake: {total_calories}\n")
        f.write(f"Average calories per meal: {average_calories:.2f}\n")
        f.write(f"Daily calorie limit: {limit}\n")
        f.write(f"Status: {status}\n")

    print(f"Report saved successfully as '{filename}'")
