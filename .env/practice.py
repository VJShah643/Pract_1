n = 5
arr = [2, 3, 6, 6, 5]
arr = sorted(arr, reverse=True)
new = []
for i in arr:
    if i not in new:
        new.append(i)

print(new[1])