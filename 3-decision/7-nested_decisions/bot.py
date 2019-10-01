#ask about book and binding
print("what type of cover does the book have (soft or hard)")
cover = str(input())

if cover == "soft":
    print("is it perfect bound? (yes/no)")
    binding = str(input())
    if binding == "yes":
        print("Soft cover, perfect bound books are very popular")
    else:
        print("Books with hard covers can be more expensive!")
elif cover == "hard":
    print("Books with hard covers can be more expensive!")
else:
    print("I don't understand what you mean")
