
""" 
2
3
1 3 1
2 1 2
3 3 3
3
0 2 1
1 1 1
2 0 0

 """

""" 
Impossible
Possible
"""


# q number of queries
# n number of containers and ball types


first = [[999336263, 998799923], [998799923, 999763019]]
third = [[1, 3, 1], [2, 1, 2], [3, 3, 3]]
fourth = [[0, 2, 1], [1, 1, 1], [2, 0, 0]]

# check this one later
query = 2


def read_from_txt():
	f = open("container_balls2.txt", "r")
	# the first line represents the queries
	q = f.readline()
	# print(q)

	# this is the size of the matrix, so the next 3 lines will be put in a container

	for query in range(int(q)):

		n = f.readline()
		# print(f'{n}')

		container = []

		for i in range(int(n)):
			line = f.readline()
			result = list(map(int, (line.split())))
			container.append(result)

		# print(container)
		organizingContainers(container)


def organizingContainers(container):

	typesum = []
	containersum = []

	for x in range(len(container)):

		tmpcolsum = []
		tmprowsum = []

		for i in range(len(container)):
			tmpcolsum.append(container[i][x])
			tmprowsum.append(container[x][i])

		total_balls = sum(ball for ball in tmpcolsum)
		typesum.append(total_balls)

		total_containers = sum(container for container in tmprowsum)
		containersum.append(total_containers)

	print(typesum.sort())
	print(containersum.sort())

	print(typesum)
	print(containersum)

	print('Possible' if typesum == containersum else 'Impossible')


# organizingContainers(first)

read_from_txt()
