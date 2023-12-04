print("Welcome to the Tip Calculator!")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("Among how many people do you want to split the bill? "))

total_per_person = (total_bill * (1 + tip_percentage / 100)) / num_people
print(f"Each person should pay: ${total_per_person: .2f}")
