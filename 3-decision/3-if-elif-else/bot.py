#asking for input
print("Towards which direction should I paint (up, down, left or right)?")
direction = str(input())

#working out which way
if direction == "up":
    print("i am painting upwards")
elif direction == "left":
    print("i am painting to the left")
elif direction == "right":
    print("i am painting to the right")
else:
    print("i am painting downwards")