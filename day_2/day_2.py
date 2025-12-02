def check_repeat_pattern(num):
    num = str(num)
    k = len(num)
    if k % 2 != 0:
        return 0
    
    if num[:k//2] == num[k//2:]:
        return int(num)
    return 0

# Get our input
with open("day_2/input.csv") as f:
    ids = f.readline()

# Build list of id ranges
ranges = []
start, stop = "", ""
curr = 0

# Iterate over input. Start appending to start_stop[0] until a dash, then append to start_stop[1] until comma, then repeat
for ch in ids:
    if ch == ",": # End of range reached, save identified values
        ranges.append([int(start), int(stop)])
        start, stop = "", ""
        curr = 0
    elif ch == "-": # End of first value reached, begin traversing second value
        curr = 1
    else:
        if curr == 0:
            start += ch
        else:
            stop += ch

# Append final range after loop (no comma to stop)
ranges.append([int(start), int(stop)])

print(ranges)

# Calculate repeat patterns within ranges

total = 0

for pair in ranges:
    for i in range(pair[0],pair[1]+1):
        total += check_repeat_pattern(i)

print(total)