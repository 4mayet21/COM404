#ask for room
print("where should I look?")
room = str(input())

#figure out what is found per room
if room == "bedroom":
    print("where in the " + room + " should I look?")
    location = str(input())
    if location == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")
elif room == "bathroom":
    print("where in the " + room + " should I look?")
    location = str(input())
    if location == "under the bed":
        print("Found a rubber duck but no battery")
    else:
        print("It is wet but I found no battery." )
elif room == "lab":
    print("where in the " + room + " should I look?")
    location = str(input())
    if location == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")
else:
    print("I do not know where that is but I will keep looking.")