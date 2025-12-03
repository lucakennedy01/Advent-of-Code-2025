def check_repeat_pattern_many(num):
    # Sliding window approach

    num = str(num)
    if not num:
        return 0

    n = len(num)

    # Try every possible pattern length (half length is max)
    for k in range(1, n//2 + 1):
        if n % k != 0:
            continue # we can ignore pattern lengths that can't divide string length

        pattern = num[:k] # Slice num up to current pattern length
        ok = True

        # Slide through string in windows of size k
        for i in range(0, n, k):
            if num[i:i+k] != pattern:
                ok = False
                break
        
        if ok:
            print(int(num))
            return int(num)
    
    return 0

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
        total += check_repeat_pattern_many(i)

print(total)