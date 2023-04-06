# Inputs
name = input ("what is your name?\n")
year_of_birth = int(input("Hi %s, what year were you born?\n" %name))
yearly_salary = float(input ("what is your yearly salary?\n"))
weekly_hours = float(input ("how manyhours do you work per week?\n"))

#Extra variable for calculations
current_year = 2022
number_of_week-in_a_year = 52

# Calculations
age = current_year - year_of_birth
hourly_salary = yearly_salary / (weekly_hours * number_of_week_in_a_year)

# Output)
print ("ok %s! you are %s year(s) old and you earn $%s/hour" %(name, age, hourly_salary))