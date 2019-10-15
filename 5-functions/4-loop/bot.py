def cross_bridge(steps):
    for step in range(0,steps):
        print('crossed step')
    if steps > 5:
        print("We must Keep going")
    else:
        print("The bridge is collapsing")
cross_bridge(3)
cross_bridge(6)
