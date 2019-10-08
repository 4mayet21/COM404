distance = int(input("how many steps are we from the cave?  "))

for step in range(0, distance):
    print(str(distance) + " steps remaining")
    distance = distance - 1

print("we have reached the cave")