#Asking question and awaiting response
print("how many zones must I cross?")
zones = int(input())

#variable to be used and modified within loop
zoneCross = zones

print("Crossing zones...")
#loop to print "crossed zone" based on input and print descending zoneCross
for zone in range(0, zones):
    print("...crossed zone " + str(zoneCross))
    zoneCross = zoneCross - 1

print("Crossed all zones. Jumanji!")