def get_input():
    columns = []

    with open('day_6/input.txt') as f:
        lines = [line.strip() for line in f if line.strip()]

    for line in lines:
        tokens = line.split()

        # convert numeric tokens to int, leave operators as strings
        row = []
        for t in tokens:
            try:
                row.append(int(t))
            except ValueError:
                row.append(t)  # operator

        # ensure columns list is wide enough
        while len(columns) < len(row):
            columns.append([])

        # add row items into columns
        for i, item in enumerate(row):
            columns[i].append(item)

    return columns


# Part 1
sums = get_input()
total = 0

def eval_colum(col):
    *nums, op = col

    result = nums[0]
    for num in nums[1:]:
        result = eval(f"{result}{op}{num}")
    return result

for sum in sums:
    total += eval_colum(sum)
print(f"Part 1 result: {total}")

# Part 2

# New function to read in input in new format
# Read column by column, reading the operator (always in first column of new sum sequence)
with open("day_6/input.txt") as f:
    lines = [line.rstrip("\n") for line in f if line.strip()]
    # Transpose into columns
    columns = [list(row) for row in zip(*lines)] 

numbers = []
total = 0
current_problem = []

for i in range(len(columns) - 1, -2, -1):
    if i == -1 or all(c == " " for c in columns[i]):
        # Solve current problem
        if current_problem:
            operator = current_problem[-1][-1] # get operator
            numbers = [] # start getting numbers in current operation
            for num in current_problem:
                numbers.append(int("".join(num[:-1]))) # get all except last
            #print(numbers)
            
            # Evaluate
            print(numbers)
            t = numbers[0]
            print(t)
            for num in numbers[1:]:
                print(num)
                res = eval(f"{t}{operator}{num}")
                print(f"{t}{operator}{num}={res}")
                t= res
            total += t
 
        current_problem = []
    else:
        # Continue building expression
        current_problem.append(columns[i])
    #print(columns[i])

print(f"Part 2 result: {total}")

    

