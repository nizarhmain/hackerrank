input1 = [50, 28, 50, 4]
input2 = [50, 29, 50, 4]
input3 = [50, 28, 50, 4]
input4 = [50, 28, 50, 4]

votes = []


def decideVote(tmp):
	max_pain = max(tmp)
	counter = 0

	max_index = []

	for i in range(len(tmp)):
		if(tmp[i] == max_pain):
			max_index.append(i)
			counter += 1

	if len(max_index) == 1:
		votes[max_index[0]] += 1

	return votes


def compareTriples(*arr):

	global votes

	# figure out how many we users
	votes = [0] * len(arr)

	for x in range(len(arr[0])):
		tmp = []
		for ar in range(len(arr)):
			# find max
			tmp.append(arr[ar][x])
		#print(tmp)
		decideVote(tmp)

	return votes
		#print(tmp)

compareTriples(input1, input2, input3, input4 )

print(votes)
