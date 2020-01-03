## Part B: Saving, with a raise

# User inputs

annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# Constants and pre-calcualated values

monthly_salary = annual_salary / 12
monthly_salary_saving = monthly_salary * portion_saved

portion_down_payment = 0.25 
down_payment = total_cost * portion_down_payment

annual_return_rate = 0.04
monthly_return = annual_return_rate / 12

# Initial values

current_savings = 0.0
numer_of_months = 0

while current_savings < down_payment:    
    current_savings += current_savings * monthly_return 
    current_savings += monthly_salary_saving

    numer_of_months += 1

    # Increase salary on each 6 month
    if numer_of_months % 6 == 0:
        monthly_salary *= 1 + semi_annual_raise
        monthly_salary_saving = monthly_salary * portion_saved

print("Number of months: " + str(numer_of_months) + "\n")