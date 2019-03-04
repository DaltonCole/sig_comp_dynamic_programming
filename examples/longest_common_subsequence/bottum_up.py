
string1 = input()
string2 = input()

memoizing = {}

# Keeps track of the number of times function is called. Reference because numbers are weird.
times_called = [0]

def longest_common_subsequence(i, j):
	times_called[0] += 1

	# Base Case
	if i == -1 or j == -1:
		memoizing[(i, j)] = 0
		return

	if string1[i] == string2[j]:
		if (i - 1, j - 1) not in memoizing:
			longest_common_subsequence(i - 1, j - 1)

		memoizing[(i, j)] = 1 + memoizing[(i - 1, j - 1)]
				
	else:
		if (i - 1, j) not in memoizing:
			longest_common_subsequence(i - 1, j)
		if (i, j - 1) not in memoizing:
			longest_common_subsequence(i, j - 1)

		memoizing[(i, j)] = max(memoizing[(i - 1, j)], memoizing[(i, j - 1)])



for i in range(-1, len(string1)):
	for j in range(-1, len(string2)):
		longest_common_subsequence(i, j)

print("Answer: {}\nTimes called: {}".format(memoizing[(len(string1) - 1, len(string2) - 1)], times_called[0]))
print("Size of table: {}".format(len(memoizing)))


def lcs_string(i, j):
	# Base case
	if i == -1 or j == -1:
		return ""

	if memoizing[(i, j)] == memoizing[(i-1, j)]:
		return lcs_string(i-1, j)
	elif memoizing[(i, j)] == memoizing[(i, j-1)]:
		return lcs_string(i, j-1)
	else:
		return string1[j] + lcs_string(i-1, j-1)

print(lcs_string(len(string1) - 1, len(string2) - 1)[::-1])