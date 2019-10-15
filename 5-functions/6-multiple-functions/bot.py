def display_ladder(steps):
    print(steps)



def create_ladder():
    bar = "| |"
    rung = "***"
    steps = input("how many steps remain? ")
    display_ladder(steps)
    for step in range(0, int(steps)):
        print(bar)
        print(rung)
    if int(steps) > 0:
        print(bar)

create_ladder()
    
    

