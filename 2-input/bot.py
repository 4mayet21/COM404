print("What is your name, Human?")
name = input()
print("Hello " + name + ". I am going to remove your liver, do you consent? Please answer yes or no")
response = input()
deathSaw = " Engaging buzzsaw, you may feel a small pinch. followed by some unbearable pain."
if response == "yes":
    print("excellent." + deathSaw)
elif response == "no":
    print("No is not a valid answer." + deathSaw)
else:
    print("Does Not Compute. WARNING! WARNING! SYSTEM ERROR!")