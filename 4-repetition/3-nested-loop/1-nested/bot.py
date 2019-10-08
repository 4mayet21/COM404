rows = int(input("how many rows should I have?  "))
cols =  int(input("how many columns should I have?  "))
face = ":-)"
print("here I go")
for row in range(0, rows):
    for col in range(0, cols):
        print(face, end="")
    print()

print("done!")