health = 100

print("Your health is 100% escape is in progress")
#blank lines for ease to read in console
print("")

#For loop to diplay questions 5 times
for num in range(0, 5):
    print("...Oh dear, who is that? ")
    who = input()
    if who == "Smiler\'s Bot":
        health = health - 20
        print("time to jam out of here!")
        print("")
    elif who == "Hacker":
        health = health + 20
        print("Yay! Better follow this one")
        print("")
    else:
        print("Phew, just another emoji!")
        print("")

print("Escaped! Health is: " + str(health) + "%")