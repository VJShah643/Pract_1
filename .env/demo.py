# bin() gives binary form of an integer in string
# insert and append are the methods to add an element to the list
# remove, del and pop are the methods to delete the element in a list

a = [5, 11, 29, 24, 29, 11, 4, 29, 24]
b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# a = b
# print(a)

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            if j not in b:
                b.append(j)

# print(b)
ctr = 0
for i in b:
    a.remove(a[i - ctr])
    ctr += 1
print(a)

# [5, 11, 29, 24, 4]
