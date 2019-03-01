
string1 = input()
string2 = input()

# Keeps track of the number of times function is called. Reference because numbers are weird.
times_called = [0]

def longest_common_subsequence(i, j):
	times_called[0] += 1

	# Base Case
	if i == -1 or j == -1:
		return 0

	if string1[i] == string2[j]:
		return 1 + longest_common_subsequence(i - 1, j - 1)
	else:
		return max(longest_common_subsequence(i - 1, j), \
					longest_common_subsequence(i, j - 1))


lcs = longest_common_subsequence(len(string1) - 1, len(string2) - 1)

print("Answer: {}\nTimes called: {}".format(lcs, times_called[0]))