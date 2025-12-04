# Part 1
# Choose 2 in order to find max value

total = 0

with open("day_3/input.csv") as f:
    for line in f.readlines():
        line = line.strip()
        values = list(map(int, line))
        n = len(values)

        max_right = [0] * n
        max_right[-1] = -1 # Last digit in each line has no value to the right, so we never choose this value

        
        # Iterate backwards over values, mapping the largest value to the right of it
        # to a matching index in new array max_right
        for i in range(n - 2, -1, -1) :
            max_right[i] = max(max_right[i+1], values[i + 1])
        
        best = -1
        for i, d in enumerate(values):
            if max_right[i] >= 0: # Include all except our last digit (we have to choose exactly 2)
                candidate = d * 10 + max_right[i]
                best = max(best, candidate)
        
        total += best

print(total)

# Part 2
# Choose 12 in order to build largest 12 digit number
# We need to slice the list of values to n-(remaining picks) and grab the largest value

total = 0

with open("day_3/input.csv") as f:
    for line in f.readlines():
        values = list(map(int,line.strip()))
        k = 12 # no. of picks

        stack = []
        to_remove = len(values) - k # how many digits we are allowed to drop. If our line is 18 values, we can drop 6 values total

        # 123456789123456789
        # 987654321987654321

        for d in values:
            # Pop smallest digits while we can still complete 12 digits
            # I.e. if the last value on the stack is smaller than the current targeted one, pop the smaller one, replacing it with the larger
            # Once to_remove = 0, we have to just append whatever comes next until the end of the line
            while stack and to_remove > 0 and stack[-1] < d:
                stack.pop()
                to_remove -= 1

            stack.append(d)
            
        # Trim if stack is too long
        total += int(''.join(map(str,stack[:k])))

        

print(total)
        
