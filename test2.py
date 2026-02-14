li = [10,54,24,52,6,71,18,9]
max1 = max2 = float('-inf')

for x in li:
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2 and x != max1:
        max2 = x
print("Second largest element is:", max2)