#asking for input

avoidNum = int(input("How many live cables must I avoid?"))
cabNum = 0

#loop
while avoidNum > 0:
    cabNum = cabNum + 1
    print("Avoiding... done! " + str(cabNum) + " live cables avoided") 
    avoidNum = avoidNum - 1

print("all live cables have been avoided")