print("Welcome to the tip calculator.")
bill = input("what was the total bill? $")
bill = float(bill)
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
percentage = int(percentage)
num_of_split = input("How many people to split the bill? ")
num_of_split = int(num_of_split)
result = bill / num_of_split * (1+ percentage / 100)
result = "{:.2f}".format(result)
print(f"Each person should pay: ${result}")