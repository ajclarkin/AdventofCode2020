import numpy as np

data = [int(line) for line in open('input.txt').read().split('\n')]

# Convert the list to a numpy array
d1 = np.array(data)

# Add every value to itself
sum_values = np.add.outer(d1, d1)
loc = np.where(sum_values == 2020)

# There will be two possibilities found: v1 + v2 and V2 + v1; take the first instance when addressing loc
print(f'The product of {d1[loc[0][0]]} and {d1[loc[0][1]]} and the solution to part 1 is ' + str(d1[loc[0][0]] * d1[loc[0][1]]))