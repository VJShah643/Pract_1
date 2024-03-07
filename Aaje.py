# demo = {
#     "M": "Mat",
#     "Z": "Zebra",
#     "C": "Cat"
# }
#
# for keys in sorted(demo.keys()):
#     print(keys, "for", demo[keys])

# Students = {
#     "Name": ['Raja', 'Rahul', 'Armaan']
# }
#
# Students["Name"].append('Riddhima')
#
# print(Students)

prices = {
    1: 0,       # Under 3
    2: 10,      # Between 3 and 12
    3: 15       # Above 12
}
num = 1
# people = {1: 0, 2: 0, 3: 0}
bill = 0

print("If you want to add another person, PRESS 1\nIf you want your final bill, PRESS 0")

while num:
    num = int(input("Enter your choice: "))
    if num == 0:
        break
    k = int(input("Select age group: \n 1 for 'Less than 3' \n 2 for 'Between 3 and 12' \n 3 for 'More than 12' \n Enter: "))
    if k in prices.keys():
        bill += prices[k]    # people[k] += 1
    else:
        print("not a valid choice")


# for k in people.keys():
#     bill += people[k]*prices[k]

print("*"*20)
print("Your total bill is: $", bill)
print("*"*20)

