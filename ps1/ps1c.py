## Part C: Finding the right amount to save away

# User inputs

annual_salary = float(input("Enter your annual salary: "))

# Constants and pre-calcualated values

semi_annual_raise = .07

annual_return_rate = .04
monthly_return_rate = annual_return_rate / 12

total_cost = float(1000000)
portion_down_payment = 0.25 
down_payment = total_cost * portion_down_payment

monthly_salary = annual_salary / 12

number_of_months = 36
epsilon = 100 
estimation_high = 10000
estimation_low = 0

high = estimation_high
low = estimation_low
number_of_guess = 0
current_savings = 0.0
guess_rate = (high + low) / 2
stop = False

while abs(down_payment - current_savings) > epsilon:

    # reset values    
    current_savings = 0.0
    monthly_salary = annual_salary / 12

    for month in range(1, number_of_months + 1):
        current_savings += current_savings * monthly_return_rate 
        current_savings += monthly_salary * (guess_rate / 10000)
        
        # Increase salary on each 6 month
        if month % 6 == 0:
            monthly_salary *= 1 + semi_annual_raise

    if current_savings < down_payment:
        low = guess_rate
    else:
        high = guess_rate

    new_rate = round((high + low)/2)

    if new_rate == guess_rate:
        stop = True
        break
    
    guess_rate = new_rate
    number_of_guess += 1

if stop == True and new_rate == estimation_high:
    print("It is not possible to pay the down payment in three years.\n")
else:
    print("Best savings rate: " + str(guess_rate / 10000))
    print("Steps in bisection search: " + str(number_of_guess) + "\n")