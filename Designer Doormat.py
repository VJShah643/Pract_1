l = 11
b = 33
wel = int(l/2)
wel_mid = int((b-7)/2) - 1
msg = "WELCOME"
pattern = 1
limit = int((b - 6)/3)
flag = 0
print(limit)

for i in range(l):
    if i == wel:
        for j in range(b - len(msg)):
            print("-", end="")
            if j == wel_mid:
                print(msg, end="")
                continue
        flag = 1
        pattern = limit
        print("")
        continue

    for j in range(b - (pattern * 3) + 1):
        if j == int((b - (pattern * 3) + 1)/2):
            print(".|." * pattern, end="")
            continue
        print("-", end="")
    if flag == 0:
        # print(pattern)
        pattern = pattern + 2
    # elif pattern == b:
    #     pattern = pattern - 2
    else:
        pattern = pattern - 2
    print("")


