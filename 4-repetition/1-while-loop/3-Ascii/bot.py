#asking for input

chargeNum = int(input("how many bars should be charged?"))
# barNum tracks value, barDisp displays value
barNum = 0
barDisp = ""
while barNum < chargeNum:
    barNum = barNum + 1
    barDisp = barDisp + "█"
    print("Charging: " + barDisp)

print("the battery is full")