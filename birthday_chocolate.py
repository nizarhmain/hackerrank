
def birthday(s, d, m):
    # print(s, d, m)
    # 2 consecutive choclates with sum 4
    # good_bits = []
    counter = 0

    if len(s) == 1:
        if s[0] == d:
            print(1)
            return

    for i in range(len(s)):
        try:
            if sum(s[i:m+i]) == d:
                counter += 1

        except IndexError as identifier:
            print(' we done')


    print(counter)


# s=[1, 2, 1, 3, 2]
s = [4]
d=4
m=1

#print(s[0:3])

birthday(s, d, m)
