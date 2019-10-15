def sum_weights(beep, bop):
    sumWeight = int(beep) + int(bop)
    return sumWeight

def calc_avg_weight(beep, bop):
    avgWeight  = ((int(beep) + int(bop))/2)
    return avgWeight

def run():
    beep = input("what is beep's weight: ")
    bop = input("what is bop's weight: ")
    calcType = input("what would you like to calculate (sum or average)?  ")
    if calcType == "sum":
        answer = sum_weights(beep, bop)
        print(answer)

    elif calcType == "average":
       answer =  calc_avg_weight(beep, bop)
       print(answer)
    else:
        print("what are you talking about?")

run()