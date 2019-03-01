# Run time O(nS) where n is number of items and S is max size

size = []
value = []

number_of_inputs = int(input())
max_bag_size = int(input())

for i in range(number_of_inputs):
	# Very useful way of taking in int input in python
	a, b = map(int, input().split(' '))
	size.append(a)
	value.append(b)

##### START ####

memoize = {}

def knap(items_left, space_left):
	# If no items left, then no value
	if items_left == 0:
		return 0

	# If we've already found this solution return it!
	if (items_left, space_left) in memoize:
		return memoize[(items_left, space_left)]

	result = 0

	# Item too big
	if size[items_left - 1] > space_left:
		# Go to "next" item
		result = knap(items_left - 1, space_left)
	else: # Item can fit
		# Max of:
		#	Current item + best with less weight
		# 	Best without current item
		result = max(value[items_left - 1] + knap(items_left - 1, space_left - size[items_left - 1]),\
			knap(items_left - 1, space_left))

	# MemoRize result
	memoize[(items_left, space_left)] = result
	return result

answer = knap(len(size), max_bag_size)
print("Max value: {}".format(answer))