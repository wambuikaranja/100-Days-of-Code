
print("Welcome to the tip calculator")

#Input the total bill amount
bill = float(input("What was the total bill? \n$"))

#Calculate the tip amount
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))

#How many people are contributing to the total bill
people = int(input("How many people to split the bill?\n"))

#Calculate the bill plus tip
bill_with_tip = tip / 100 * bill + bill

#find the share per person
share_per_person = round(bill_with_tip / people, 2)

#format the share per person into 2dp
share_per_person = "{:.2f}".format(share_per_person)
print(f"Each person should pay ${share_per_person}")