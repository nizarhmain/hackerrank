
a = [4, 6, 5, 3, 3, 1]
b = [1, 2, 2, 3, 1, 2]

c = "4 2 3 4 4 9 98 98 3 3 3 4 2 98 1 98 98 1 1 4 98 2 98 3 9 9 3 1 4 1 98 9 9 2 9 4 2 2 9 98 4 98 1 3 4 9 1 98 98 4 2 3 98 98 1 99 9 98 98 3 98 98 4 98 2 98 4 2 1 1 9 2 4"

c.split()

map_object = map(int, c.split())
list_of_integers = list(map_object)

c = list_of_integers

def createSub(number, occurence):
    return [number] * occurence

#define the function#


def find_max_list(list):
    list_len = [len(i) for i in list]
    return list_len.index(max(list_len))


def merge(subs):

    # take the longest sub array and check if it can be merged

    # print(subs)

    # find the longest list with -1 or +1

    bigboi = find_max_list(subs)

    target = subs[bigboi][0]

    below = target - 1
    above = target + 1

    longest = 0

    for i in range(len(subs)):
        if subs[i][0] == below:

            if len(subs[i]) > longest:
                longest = len(subs[i])

            # print('you are a bottom')

        if subs[i][0] == above:

            if len(subs[i]) > longest:
                longest = len(subs[i])

            # print('you are a top')

    # print(longest)

    return longest + len(subs[bigboi])


def pickingNumbers(a):
    # we can't reduce the space complexity here, 3 - 3 = 0

    # start looking for duplicates

    a.sort()

    subs = []

    for i in range(len(a)):

        number = a[i]

        try:

            next_number = a[i+1]

            if next_number == number:
                continue

            # print(number)

            # does this number have a duplicate in the list
            # is the next number equal to this one
            occurences = a.count(number)
            # print(occurences)

            subs.append(createSub(number, occurences))

            pass
        except IndexError:
            # print(number)
            occurences = a.count(number)
            # print(occurences)
            # print('-------------')
            subs.append(createSub(number, occurences))

            pass

    return merge(subs)


print(pickingNumbers(c))
