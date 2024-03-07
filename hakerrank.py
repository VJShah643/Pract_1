s = "aabbbccde"
count = {}
for i in s:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
# print(count)
char = sorted(count)
# print(char)
final_dict = {}
for i in char:
    final_dict[i] = count[i]
# print(final_dict)

val = []
for i in count.values():
    if i not in val:
        val.append(i)
val.sort(reverse=True)
# print(val)
new = []

for i in range(len(val)):
    for k, v in final_dict.items():
        if v == val[i]:
            new.append(k)
new = new[:3]
for i in new:
    print(i, final_dict[i])
