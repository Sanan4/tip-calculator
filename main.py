#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to tip calculator!")

total_bill = input("what was your total bill? $")

total_tip = input("How much tip would you like to give? 10, 12, or 15? ")

people_split = input("How many people to split the bill? ")

new_total_tip = float(total_tip) / 100

bill_each_person = float(total_bill) / float(people_split) * (1 + new_total_tip)

final_amount = "{:.2f}".format(bill_each_person)

print(f"Each person should pay: ${final_amount} ")
