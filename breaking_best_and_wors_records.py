

scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]


def breakingRecords(scores):

    print(scores)

    min_increase = 0
    max_increase = 0

    min = scores[0]
    max = scores[0]

    for i in range(len(scores)):

        if scores[i] > max:
            max_increase += 1
            max = scores[i]

        if scores[i] < min:
            min_increase += 1
            min = scores[i]

    print(str(max_increase) + ' ' + str(min_increase))


breakingRecords(scores)
