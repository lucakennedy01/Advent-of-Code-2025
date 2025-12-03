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

print("part 1 zeros:", zeros)
zeros = 0
dial = 50

with open("day_1/input.csv") as f:
    
    for x in f:
        x = x.strip()
        direction = x[0]
        value = int(x[1:])

        # Incremental approach
        step = 1 if direction == "R" else -1

        for _ in range(value):
            dial = (dial + step) % 100
            if dial == 0:
                zeros += 1

       

print(f"part 2 zeros: {zeros}")
