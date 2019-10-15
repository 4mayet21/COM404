#stepR is steps remaining, stepC is steps crossed
def climb_ladder(stepC,stepR):
    if stepC >= stepR:
        print("we made it")
    else:
        print("still some way to go")

climb_ladder(2,5)
climb_ladder(5,5)