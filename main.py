# Input your current age here
age = input("What is your current age? ")

# Calculate for days, weeks and months in 90years
days = 365 * 90
weeks = 52 * 90
months = 12 * 90

# Calculate the days, weeks and months left to live, from present age until 90years 
days_left = (days) - (int(age) * 365)
weeks_left = (weeks) - (int(age) * 52) 
months_left = (months) - (int(age) * 12)

# Using the f-string, print your remaining time on earth
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")