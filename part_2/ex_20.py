year = int(input("Year: "))
input_year = year

while True:
    year += 1
    if year % 4 == 0 and (year % 100 != 0 and year % 400 != 0):
        break
    elif year % 100 == 0 and year % 400 == 0:
        break
print(f"The next leap year after {input_year} is {year}")