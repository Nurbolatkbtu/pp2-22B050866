def solve(numheads, numlegs):
    numRabbit = numlegs / 2 - numheads
    numChicken = numheads - numRabbit
    print(int(numChicken))
    print(int(numRabbit))
solve(35, 94)