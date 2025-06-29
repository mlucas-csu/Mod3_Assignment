# Part 1: Calculate total amount of a meal purchased at a restaurant

# User inputs the cost of their meal from the receipt
meal_only_price = float(input("Enter the meal cost on the receipt: $"))
formatted_meal_only_price = float(f"{meal_only_price:.2f}")
print(f"The meal cost was ${formatted_meal_only_price}")

# Defining the value of the tip and sales tax as floats
tip_percentage = 0.18
sales_tax = 0.07

# Calculating the dollar amounts for the tip and sales tax then formatted those values for output to 2 decimal places
tip_amount = formatted_meal_only_price * tip_percentage
print("For an 18% tip, the total amount to tip will be ${:.2f}".format(tip_amount))
sales_tax_amount = formatted_meal_only_price * sales_tax
print("With a sales tax of 7%, you will have to pay ${:.2f} in taxes".format(sales_tax_amount))

# Putting it all together
total_meal_price = formatted_meal_only_price + tip_amount + sales_tax_amount
print("In total, the meal will cost ${:.2f}".format(total_meal_price))


# Part 2: Keeping time with a 24 hour clock

# User inputs the time in hours
current_time_in_hours = int(input("Please input the current time in hours (e.g. if it is 9 pm input 21): "))

# User inputs the number of hours until their alarm goes off
hours_until_alarm = int(input("Please input how many hours until your alarm goes off: "))

# Obtain the integer for the total hours until the alarm goes off
alarm_total_hours = current_time_in_hours + hours_until_alarm

# Find time on 24-hour clock when alarm goes off
alarm_time = alarm_total_hours % 24
print(f"On a 24-hr clock, the alarm will go off at the time of {alarm_time}")




