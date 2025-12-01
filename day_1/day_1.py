dial = 50
zeros = 0

with open("day_1/input.csv") as f:
    for x in f:
        x = x.strip()
        direction = x[0]
        value = int(x[1:])

        if direction == "R":
            dial += value
        else:
            dial -= value

        dial %= 100 

        if dial == 0:
            zeros += 1

print("zeros:", zeros)