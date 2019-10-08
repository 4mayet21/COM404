num = int(input("please enter a number:  "))
numFact = 1
while num > 0 :
    numFact = numFact * num
    num = num-1

print("The Factorial is " + str(numFact))