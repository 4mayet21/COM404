#ask for 3 numbers
print("please enter a whole number")
num_first = int(input())
print("please enter a second whole number")
num_second = int(input())
print("please enter a third whole number")
num_third = int(input())

#modulo to make o or 1 (maybe?)
num_first_rem = num_first % 2
num_second_rem = num_second % 2
num_third_rem = num_third % 2

#count how many odds and evens
if num_first_rem + num_second_rem + num_third_rem == 0:
    print("there are 3 evens")
elif num_first_rem + num_second_rem + num_third_rem == 1:
    print("there are 2 evens and 1 odd")
elif num_first_rem + num_second_rem + num_third_rem == 2:
    print("there are 2 odds and 1 even")
else:
    print("there are 3 odds")