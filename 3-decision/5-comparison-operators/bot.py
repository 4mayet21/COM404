# asking for 2 variables
print("please enter a number")
num_first = float(input())
print("please enter a second number")
num_second = float(input())

#comparing two numbers
if num_first > num_second:
    print("the second number is smallest")
elif num_first < num_second:
    print("the first number is smallest")
else:
    print("they are both the same")