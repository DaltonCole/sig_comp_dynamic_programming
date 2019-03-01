_, cost = input().split()
cost = int(cost)

# List of ints of times
times = list(map(int, input().split()))

# List of times - cost
profitability = []
for num in times:
	profitability.append(num - cost)

max_so_far = 0
max_ending_here = 0

for cost in profitability:
	# Include the break
	max_ending_here += cost
	# If including the break leads us to the negatives, don't to it!
	if max_ending_here < 0:
		max_ending_here = 0

	# If current best is better, it becomes the new best
	if max_so_far < max_ending_here:
		max_so_far = max_ending_here

print(max_so_far)

# Discussion: How is this dynamic programming? Where's the recursion??
#	* Is this top-down or bottom-up?