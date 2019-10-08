#asking for input
phrase = input("please enter a phrase:  ")
bopLen = (len(str(phrase)))
bops = ""
while bopLen > 0:
    bops = bops + "bop "
    bopLen = bopLen - 1

print(bops)