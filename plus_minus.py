arr = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0

    for num in arr:
        if (num > 0):
            pos += 1
        elif (num < 0):
            neg += 1
        else:
            zer += 1

    print("{0:.6f}".format(pos / len(arr)))
    print("{0:.6f}".format(neg / len(arr)))
    print("{0:.6f}".format(zer / len(arr)))


plusMinus(arr)
      

