from collections import Counter

def migratoryBirds(arr):

    birds = open("birds.txt","r") 

    stuff = birds.readline().split(' ')
    stuff.sort()
    print(Counter(stuff).most_common(10))

arr = [1, 1, 2, 2, 3]

migratoryBirds(arr)