numNum = int(input("how many numbers should I add up:  "))

numAns = 0

numQNum = 1

numNumMod = numNum

while numNum > 0:
    numAdd = input("please enter number " + str(numQNum) + " of " + str(numNumMod) + ":  ")
    numAns = numAns + int(numAdd)
    numNum = numNum - 1
    numQNum = numQNum + 1

print("the Answer is " + str(numAns))