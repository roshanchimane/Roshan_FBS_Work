
total_days = int(input("Enter the number of days: "))

years = total_days // 365
remaining_days_after_years = total_days % 365

weeks = remaining_days_after_years // 7
remaining_days = remaining_days_after_years % 7

print(f"{total_days} days is equivalent to {years} years, {weeks} weeks, and {remaining_days} days.")
