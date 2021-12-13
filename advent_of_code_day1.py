# Advenet of Code 2021 Day 1

with open("./data.txt") as f:
    depths = []

    # For every line in the file
    for line in f:
        depths.append(int(line))
        # Add the integer to a list of depths
print(depths)

for i in range(1999):
    num_increase = 0
    num_decrease = 0
    x = 1
    x += 1
    if depths[x+1] > depths[x]:
        num_increase += 1
    else:
        num_decrease += 1
    print(f"{num_increase}")
