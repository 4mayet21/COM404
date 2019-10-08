bright = int(input("what level of brightness is required:   "))
beep = "**"
bop = "**"

print("Adjusting brightness...")
for lumen in range(0, bright,2):
    print("Beep's brightness level: " + beep)
    print("Bop's brightness level: " + bop)
    beep = beep + "**"
    bop = bop + "**"

print("adjustments complete")
