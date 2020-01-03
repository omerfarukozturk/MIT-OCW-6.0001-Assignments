## Part A: House Hunting

# User inputs

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

# Constants and pre-calcualated values

monthly_salary_saving = (annual_salary / 12) * portion_saved

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

print("Number of months: " + str(numer_of_months) + "\n")