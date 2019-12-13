
arr = [1,2,3,4,5]


def miniMaxSum(arr):

    minis = []
    maxis = []

    arr1 = arr.copy()
    arr2 = arr.copy()

    #print(arr2)

    # will run 4 times
    for i in range(len(arr) - 1):
        minis.append(min(arr1))
        small = arr1.index(min(arr1))
        del arr1[small]

        maxis.append(max(arr2))
        big = arr2.index(max(arr2))
        del arr2[big]

    print(f'{sum(minis)} {sum(maxis)}') 


miniMaxSum(arr)
