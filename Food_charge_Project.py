"""
This is the script for generating the grand total amount of a meal purchased with tips and the sales tax.

Written By: Bolarinwa Joseph Oyerinde - Cloud Engineer Trainee
Institution : Azubi Africa 
Course: Cloud Engineering
Class : Spring 2023
Version: 1.0
Revisions: None

"""

# Enter the charge for the food
food_charge = input('Enter the charge for the food: $')
food_charge = float(food_charge)  # convert the string data type output from above to numeric data type
print(f'Food charge = ${food_charge:.2f}') # Display the food charge and use f-string to format it to 2 decimal places

# Calculate the tip based on the food charge and round it up to 2 decimal places
tip = 18/100 * food_charge    # calculate the tip charge which is 18% of the food charge
print(f'Tip = ${tip:.2f}')     # Display the tip charge and use f-string to format it to 2 deciaml places

# Calculate the Sales tax based on the food charge and round it up to 2 deciaml places
sales_tax = 7/100 * food_charge  # calculate the sales tax charge which is 7% of the food charge
print(f'Sales tax = ${sales_tax:.2f}\n')   # Display the sales tax charge and use f-string to format it into 2 deciaml places. leave an empty line


# Calculate the Grand total charge 
print(f'Grand Total = ${food_charge + tip + sales_tax:.2f}')  # display the addition of the charges for food , tip, and sales tax.
