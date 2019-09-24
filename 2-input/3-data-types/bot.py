death = "aaaaaaaaaaaaaaaaaaa"
print("what is your name human?")
name = str(input())
if name == "Sir Lancelot of Camelot":
    print("what is your quest?")
    quest = input()
    if quest == "I seek the holy grail":
        print("what is your favorite colour")
        colour = input()
        if colour == "blue":
            print("accross you go")
        else:
            print(death)
    else:
        print(death)
else:
    print("how old are you (in years)")
    age = int(input())
    print("what is your height in metres?")
    height = float(input())
    print("how much do you weigh in kg")
    weight = float(input())
    print()
    bmi = weight/(height**2)
    print(name + ", you are " + str(age) + " years old. Your BMI is: " + str(bmi))