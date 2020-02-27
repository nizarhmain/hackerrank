

def catAndMouse(values):
    x = values[0]
    y = values[1]
    z = values[2]

    distanceA = abs(x - z)
    distanceB = abs(y - z)

    if distanceA == distanceB:
        return 'Mouse C'

    if distanceA > distanceB:
        return 'Cat B'

    if distanceB > distanceA:
        return 'Cat A'

first = [1, 2, 3]
second = [1, 3, 2]


print(catAndMouse(second))