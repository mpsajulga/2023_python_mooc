weekly_cafeteria_visit = float(input("How many times a week do you eat at the student cafeteria? "))
student_lunch_price = float(input("The price of a typical student lunch? "))
week_grocery_budget = float(input("How much money do you spend on groceries in a week? "))

weekly_expenses = week_grocery_budget+ weekly_cafeteria_visit * student_lunch_price
daily_expenses = weekly_expenses/7

print("Average food expenditure:")
print(f"Daily: {daily_expenses} euros")
print(f"Weekly: {weekly_expenses} euros")