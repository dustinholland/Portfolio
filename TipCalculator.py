print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10 12 15 \n"))
people = int(input("How many people to split the bill?\n"))
subtotal = tip / 100 * bill + bill
total = round(subtotal / people, 2)
print(f"Your total for each person is ${total}")
