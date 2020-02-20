
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


first = [[1, 1], [1, 1]]
third = [[1, 3, 1], [2, 1, 2], [3, 3, 3]]
fourth = [[0, 2, 1], [1, 1, 1], [2, 0, 0]]

# check this one later
query = 2

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
    
    print(typesum)
    print(containersum)

organizingContainers(fourth)






