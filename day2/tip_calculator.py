# Print Welcome to the tip calculator.
print("Welcome to the tip calculator.")

# Input data into float and int
bill = float(input("What was your total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate tip 
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

# Calculate the total bill as per person
bill_per_person = total_bill / people

# Round up the float result of bill per person upto the second decimal
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

# Result
result = f"Each person should pay: ${final_amount}"
print(result)