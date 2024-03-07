print(1000000 - 111 + 1)

# copying list

my_food = ['Burger', 'Pizza', 'Pani puri']
Friends_food = my_food[:]
print(my_food)
print(Friends_food)

a = [1, 3, 4]
b = [2, 5, 6]
c = a + b
b.append(89)
print(a, b, c)

new_l = a.copy()
print(new_l)

# Formatted string
print(f"The new string is {new_l}")

# if... elif... else
a = 55
if a < 10:
    print(f"{a} < 10")
elif a < 60:
    print(f"{a} < 60")
else:
    print(NO)


age = int(input("Give your age: "))

if age < 2:
    print("Baby")
elif 2 <= age < 4:
    print("Toddler")
elif 4 <= age < 13:
    print("Kid")
elif 13 <= age < 20:
    print("Teenager")
elif 20 <= age < 65:
    print("Adult")
else:
    print("Elder")


# check if list is empty
if b:
    print("Not empty")
else:
    print("Empty")

# pro

Current_users = ['Raj_123', 'John_457', 'Rita_333', 'KaRiShma_420', 'Billy_000']
new_users = ['Harsh_908', 'john_457', 'Hritika_003', 'koli_678', 'Komolika_785']

for i in range(len(Current_users)):
    Current_users[i] = Current_users[i].lower()

for i in new_users:
    if i.lower() in Current_users:
        print(f"You will need to enter another username for {i}")
    else:
        print(f"{i} is available")


























