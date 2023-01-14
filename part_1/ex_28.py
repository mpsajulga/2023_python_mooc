in_wage = float(input("Hourly wage: "))
in_work = int(input("Hours worked: "))
in_day = input("Day of the week: ")

normal_daily_wage = in_wage * in_work
sunday_wage = (in_wage*2)*in_work

if in_day == "Sunday":
    print(f"Daily wages: {sunday_wage} euros")
else:
    print(f"Daily wages: {normal_daily_wage} euros")