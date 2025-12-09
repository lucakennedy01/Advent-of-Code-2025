id_bounds = []
result = 0

def get_ranges():
    all_bounds = []
    with open("day_5/input.txt") as f:
        data = f.readlines()
        for line in data:
            line = line.strip()
            if "-" not in line:
                return all_bounds
            bounds = []
            for i, c in enumerate(line):
                if c == "-":
                    bounds.append(int(line[:i]))
                    bounds.append(int(line[i+1:]))
                    all_bounds.append(bounds)

def get_ids():
    ids = []
    with open("day_5/input.txt") as f:
        data = f.readlines()
        for line in data:
            line = line.strip()
            if "-" in line or line == "":
                continue
            ids.append(int(line))

    return ids

# Part 1
ranges = get_ranges()
ids = get_ids()
print(ids)
total = 0

for id in ids:
    for r in ranges:
        if r[0] <= id <= r[1]:
            total += 1
            break

print(f"Part 1 Answer: {total}")

# Part 2
ranges = get_ranges()

total = 0
ranges = sorted(ranges)
r_temp = ranges[0]
for r in ranges[1:]:
    # current upper bound less than previous upper bound
    # current range is a subset of r_temp, pass
    if r[1] <= r_temp[1]:
        pass
    # current lower beyond r_temp range
    # r_temp is complete, sum current range inside and set r_temp to current range
    elif r[0] > r_temp[1]:
        total += 1 + (r_temp[1] - r_temp[0])
        r_temp = r
    # current lower bound inside r_temp
    # set upper bound of r_temp to our new r upper
    elif r[0] <= r_temp[1]:
        r_temp = (r_temp[0], r[1])
total += 1 + (r_temp[1] - r_temp[0])
print(f"Part 2 Answer: {total}")
            
    



        