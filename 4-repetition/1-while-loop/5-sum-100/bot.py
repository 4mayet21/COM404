print("calculating the sum of the first 100 numbers")

count = 0
tot = 0
countMod = 0
while count <= 100:
    tot = tot + countMod
    countMod = countMod + 1
    count = count + 1

print("Done the answer is " + str(tot))