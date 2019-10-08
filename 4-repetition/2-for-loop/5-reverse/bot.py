scrawl = (input("What strange markings do you see?  "))
revMod = ""
for item in range(0, len(scrawl)):
    rev = scrawl[item]
    revMod = rev + revMod


print(revMod)
