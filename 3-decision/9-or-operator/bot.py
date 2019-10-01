#asking for input
print("what sort of adventure would you like?")
advenType = str(input())

#displaying type
if ((advenType == "scary") or (advenType == "short")):
    print("entering the dark forest")
elif ((advenType == "safe") or (advenType == "long")):
    print("taking the safe route")
elif(advenType == "sexy"):
    print("please purchase the premium version of this game")
    print("not sure which route to take")
else:
    print("not sure which route to take")